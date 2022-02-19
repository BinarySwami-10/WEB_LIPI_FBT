
# import modulex as mx
from mxproxy import mx
import requests
import re

false = False
true = True
null = None


class Auth:
    """contains the testing and live auth creds"""
    live = {
        "Authentication": {
            "IpAddress": "13.126.21.116",
            "Password": "Fastbook@pS9nfqCG",
            "PortalID": "26",
            "UserName": "FastBookTrip",
            }
        }
    test = {
        "Authentication": {
            "IpAddress": "13.126.21.116",
            "Password": "EMT@uytrFYTREt",
            "PortalID": "26",
            "UserName": "EMTB2B"
            },
        }


def get_flights():
    # url="http://serviceapi.easemytrip.com/Flight.svc/json/FlightSearch"
    url = "https://stagingapi.easemytrip.com/Flight.svc/json/FlightSearch"
    # {
    #     "Adults": "1",
    #     "Infants": "0",
    #     "Childs": "0",
    #     "TraceId": "",
    #     "EngineID": ["0", "1", "5", "7", "10", "11"],
    #     "FlightSearchDetails": [
    #         {
    #             "BeginDate": "2021-12-25",
    #             "Origin": "DEL",
    #             "Destination": "AMD"
    #         }
    #     ],
    #     "TripType": 0,
    #     "Cabin": 0
    # }
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
                "BeginDate": "2022-02-22",
                "Origin": "DEL",
                "Destination": "Hyd"
                },
            ],
        "TripType": 1,
        "Cabin": 0
        }
    # print(mx.jdumps(data))
    r = requests.post(url, json=data)
    return mx.jdumps(r.json())


def post_book_flight():

    pass


if __name__ == '__main__':
    # data=get_flights()
    # print(mx.jdumps(data))

    # r=get_tbo_routes()
    r = get_flights()
    print(r)
    ...
