from fastapi import FastAPI
import uvicorn
import requests
from api.EaseMyTrip import Auth
from api.EaseMyTrip import EaseMyTrip
import os
import colorama
colorama.init()
app = FastAPI()


@app.get("/api")
def home():
    return {"Hello": os.getcwd()}


@app.get('/api/fs')
async def get_flights(src,dst):
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
                "BeginDate": "2022-03-17",
                "Origin": src,
                "Destination": dst
            },
        ],
        "TripType": 0,
        "Cabin": 0
    }
    # print(mx.jdumps(data))
    print(src)
    r = requests.post(url, json=data)
    return r.json()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
