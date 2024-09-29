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

def send_data_kafka(payload):
    headers = {
        "Content-Type": "application/json",
    }
    kafka_producer_url = f'http://kafka_producer:8325/sendKafka'
    try:
        response = requests.post(kafka_producer_url, json=payload, headers=headers)
        response_status_code = response.status_code
        if response_status_code == 200:
            print("Data published to Kafka")
        else:
            print(f"Failed to post data. Status code: {response_status_code}")
    except Exception as e:
        print(f"An error occurred while posting data: {e}")

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

    payload = {
        "service": "externalService"
    }

    try:
        _temperatureCelcius = response_dict['current']['temp_c']
        _time = response_dict['location']['localtime']
        response_data = {
            "location": _location,
            "temperature": int(_temperatureCelcius), # to ensure float/int or any values are aligned with WeatherResponse schema model specific for temperature
            "timestamp": _time,
        }
        payload = {**payload, **response_data}
        send_data_kafka(payload)
        return response_data
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")
