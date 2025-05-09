# 🌎 Geo country service API 🌎
A service to get alpha3 country code from provided coordinate point

---

# Usage

Do a request to **/getCountryCode** with payload:
```
{"latitude": 45.123 (float), "longitude": -25.123 (float)}
```
Response ```body``` contains ```message``` and ```result```. 
If coordinate payload is valid Alpha 3 country will be stored in ```result```.
---
*Example:*

Request
```
api/getCountryCode?latitude=54.769350220741586&longitude=25.319456079720805
```

Response
```
Response.body = b'{"message":"OK","result":"LTU"}'
```
