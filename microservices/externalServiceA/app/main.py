from fastapi import FastAPI, HTTPException, Depends
import asyncio
import requests
from fastapi.middleware.cors import CORSMiddleware
import os
from app.schemas.weather_schema import WeatherData, WeatherResponse
from dotenv import load_dotenv
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv()
@app.get("/")
async def server_health_check():
    return {"Status": "External Weather Service Server healthy!"}

@app.get("/externalApi/getWeather/{location}", response_model=WeatherResponse)
async def get_weather(location: str):
    url = f'http://api.weatherapi.com/v1/current.json'
    API_KEY= os.getenv('WEATHER_API_KEY')
    params = {
        'key': API_KEY,
        'q': location
    }
    response = requests.get(f'{url}', auth=None, params=params)
    response_dict = json.loads(response.text)
    _location = location
    try:
        _temperatureCelcius = response_dict['current']['temp_c']
        _time = response_dict['location']['localtime']
    except Exception as e:
        print(f'Error with API. Sending null values. Status code: {response.status_code}')
        _temperatureCelcius = 'Error'
        _time = 'Error'
    response_data = {
        "location": _location,
        "temperature": _temperatureCelcius,
        "timestamp": _time
    }
    return response_data
