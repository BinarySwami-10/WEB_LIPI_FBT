# SERVER SETUP
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from api.EaseMyTrip import Auth
# from api.EaseMyTrip import EaseMyTrip


# GENERAL IMPORTS
import os
import colorama
import requests
from pathlib import Path

import modulex as mx

# INITIALIZE
colorama.init()
app = FastAPI()


@app.get("/",response_class=HTMLResponse)
async def home():
    return mx.fread('./dev/index.html')


@app.get("/api")
def apihome():
    return {"Hello": 'This the the home of api Router '}


@app.get('/api/fs')
def get_flights(src,dst,fromdate):
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
            "11",
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
    # return {"r.json()","asdasd"}


if __name__ == "__main__":
    app.mount("/dev/", StaticFiles(directory=Path(__file__).parent, html = True), name="site")
    uvicorn.run('main:app', reload=True, workers=2)
