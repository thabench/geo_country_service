import api
import json


def test_api_ok_result():
    response = api.get_country_code(latitude=54.769350220741586, longitude=25.319456079720805)
    assert response.status_code == 200
    assert json.loads(response.body).get("result") == "LTU"


def test_api_no_country():
    response = api.get_country_code(latitude=0.1, longitude=0.1)
    response_json = json.loads(response.body)
    assert response.status_code == 400
    assert not response_json.get("result")
    assert response_json.get("message") == "Country code not found for coordinates: latitude: 0.1, longitude: 0.1"


def test_api_bad_payload():
    response = api.get_country_code(latitude=100, longitude=None)
    assert response.status_code == 400
    response_json = json.loads(response.body)
    assert not response_json.get("result")
    assert response_json.get("message") == "Bad coordinates: latitude: 100, longitude: None"
