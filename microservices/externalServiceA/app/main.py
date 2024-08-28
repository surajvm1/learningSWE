from fastapi import FastAPI, HTTPException, Depends
import asyncio
import requests
from fastapi.middleware.cors import CORSMiddleware
import os
from app.schemas.weather_schema import WeatherData, WeatherResponse
from dotenv import load_dotenv
import json
from app.kafka_producer import create_kafka_producer

app = FastAPI()
producer = create_kafka_producer()
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

    # producer.send('topic_a', {
    #     "location": 'hello',
    #     "temperature": 300,
    #     "timestamp": 'hohoho'
    # })
    # producer.flush()

    # producer.produce('topic_a', key=None, value=json.dumps({
    #     "location": 'hello',
    #     "temperature": 300,
    #     "timestamp": 'hohoho'
    # }))
    # producer.flush()


    url = f'http://api.weatherapi.com/v1/current.json'
    API_KEY= os.getenv('WEATHER_API_KEY')
    params = {
        'key': API_KEY,
        'q': location
    }
    response = requests.get(f'{url}', auth=None, params=params)
    response_dict = json.loads(response.text)
    # response_json = response.json()
    _location = location
    try:
        _temperatureCelcius = response_dict['current']['temp_c']
        # _temperatureCelcius = response_json.current.temp_c
        _time = response_dict['location']['localtime']
        # _time = response_json.location.localtime

        response_data = {
            "location": _location,
            "temperature": int(_temperatureCelcius), # to ensure float/int or any values are aligned with WeatherResponse schema model specific for temperature
            "timestamp": _time,
        }
        return response_data
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")
