# 🌎 Geo country service API 🌎
A service to get alpha3 country code from provided coordinate point

---

# Usage

Pass latitude and longitude coordinates to **get_country_code** function:
```
{"latitude": (float), "longitude": (float)}
```
Result contains ```message``` and ```result```. 
If coordinate payload is valid Alpha-3 country will be stored in ```result```.
---
*Example:*

```python
from geo_country_service import get_country_code


result = get_country_code(latitude=45.123, longitude=-25.123)
print(result)
```
*Result*
```
{"message":"success","result":"LTU"}
```
