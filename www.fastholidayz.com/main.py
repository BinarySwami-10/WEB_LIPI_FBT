# SERVER SETUP
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from api.EaseMyTrip import Auth
from api.EaseMyTrip import EaseMyTrip


# GENERAL IMPORTS
import os
import colorama
import requests
import modulex as mx

# INITIALIZE
colorama.init()
app = FastAPI()
app.mount("/", StaticFiles(directory="./dev/", html = True), name="site")


@app.get("/",response_class=HTMLResponse)
async def home():
    return mx.fread('./dev/index.html')


@app.get("/api")
def apihome():
    return {"Hello": os.getcwd()}


@app.get('/api/fs')
async def get_flights(src,dst,fromdate):
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
                "BeginDate": fromdate,
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
