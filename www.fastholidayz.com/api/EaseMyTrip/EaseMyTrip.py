try:
    import Auth
except Exception as e:
    pass

import requests

def get_flights():
    # url="http://serviceapi.easemytrip.com/Flight.svc/json/FlightSearch"
    url = "https://stagingapi.easemytrip.com/Flight.svc/json/FlightSearch"
    data = {
        "Adults": "1",
        "Childs": "0",
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
                "BeginDate": "2022-03-25",
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

if __name__ == '__main__':
    print(get_flights())