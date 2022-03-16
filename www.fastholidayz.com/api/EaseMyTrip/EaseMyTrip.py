def get_flights():
    # url="http://serviceapi.easemytrip.com/Flight.svc/json/FlightSearch"
    url = "https://stagingapi.easemytrip.com/Flight.svc/json/FlightSearch"
    data = {
        "Adults": "1",
        "Childs": "1",
        "Infants": "0",
        **Auth.test,
        "TraceId": "",
        "EngineID": [
            "0",
            "1",
            "5",
            "6",
            "7",
            "10",
            "11"
            ],
        "FlightSearchDetails": [
            {
                "BeginDate": "2022-03-15",
                "Origin": "DEL",
                "Destination": "HYD"
                },
            ],
        "TripType": 1,
        "Cabin": 0
        }
    # print(mx.jdumps(data))
    r = requests.post(url, json=data)
    return r.json()
