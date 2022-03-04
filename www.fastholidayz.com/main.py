from fastapi import FastAPI
import uvicorn
from api.API_EMT import Auth
from api.API_EMT import main_api
import os

app = FastAPI()


@app.get("/api")
def home():
    return {"Hello": os.getcwd()}


@app.get('/api/v1/flightSearch')
def get_flights():
   resp = main_api.get_flights()
   return resp


if __name__ == "__main__":
    uvicorn.run("main:app")
