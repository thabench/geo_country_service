import json
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import status
from shapely.geometry import shape


app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "world_countries.geojson")


@app.get("/getCountryCode")
def get_country_code(latitude: float, longitude: float) -> JSONResponse:
    coord_string = f"latitude: {latitude}, longitude: {longitude}"
    if not latitude or not longitude:
        bad_coordinates_response = JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": f"Bad coordinates: {coord_string}", "result": None}
        )
        return bad_coordinates_response

    alpha3_code = ""
    with open(DATA_PATH, "r") as f:
        countries = json.load(f)

    mapped_country_shapes = (
        {idx: {"shape": shape(feature["geometry"]), "countryCode": feature["properties"].get("iso_a3")}
         for idx, feature
         in enumerate(countries["features"])}
    )
    coordinates_point = shape(context={"type": "Point", "coordinates": [longitude, latitude]})

    for key, value in mapped_country_shapes.items():
        if coordinates_point.intersects(value["shape"]):
            alpha3_code = value.get("countryCode")
            break

    if not alpha3_code:
        not_found_response = JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": f"Country code not found for coordinates: {coord_string}", "result": None}
        )
        return not_found_response

    country_code_response = JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "OK", "result": f"{alpha3_code}"}
        )
    return country_code_response
