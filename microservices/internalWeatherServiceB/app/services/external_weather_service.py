import requests
import json
import asyncio
def get_weather_data_ext_service(location:str):
    try:
        external_weather_service_url = f'http://external_service_a:9900/externalApi/getWeather/{location}'
        response = requests.get(external_weather_service_url)
        if response.status_code == 200:
            weather_data = json.loads(response.text)
            return weather_data
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")
