import handler


def test_ok_result():
    result = handler.get_country_code(latitude=54.769350220741586, longitude=25.319456079720805)
    assert result["message"] == "success"
    assert result["result"] == "LTU"


def test_no_country():
    result = handler.get_country_code(latitude=0.1, longitude=0.1)
    assert not result.get("result")
    assert result.get("message") == "Country code not found for coordinates: latitude: 0.1, longitude: 0.1"


def test_bad_payload():
    result = handler.get_country_code(latitude=100, longitude=None)
    assert not result.get("result")
    assert result.get("message") == "Invalid coordinates. lat: 100, lon: None"
