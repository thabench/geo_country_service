import orjson
import os
from shapely.geometry import shape


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "world_countries.geojson")


def get_country_code(latitude: float, longitude: float) -> dict[str, str | None]:
    result = {"message": "", "result": None}
    coord_string = f"latitude: {latitude}, longitude: {longitude}"
    if not latitude or not longitude:
        result["message"] = f"Invalid coordinates. lat: {latitude}, lon: {longitude}"
        return result

    alpha3_code = ""
    with open(DATA_PATH, "rb") as f:
        countries = orjson.loads(f.read())

    mapped_country_shapes = (
        {idx: {"shape": shape(feature["geometry"]), "countryCode": feature["properties"].get("adm0_a3_us")}
         for idx, feature
         in enumerate(countries["features"])}
    )
    coordinates_point = shape(context={"type": "Point", "coordinates": [longitude, latitude]})

    for key, value in mapped_country_shapes.items():
        if coordinates_point.intersects(value["shape"]):
            alpha3_code = value.get("countryCode")
            break

    if not alpha3_code or not alpha3_code.isalpha():
        result["message"] = f"Country code not found for coordinates: {coord_string}"
        return result

    result["message"] = "success"
    result["result"] = f"{alpha3_code}"
    return result
