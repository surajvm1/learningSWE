import json
from fastapi import FastAPI
import requests
import pandas as pd
from sqlalchemy import *
import asyncio

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
"""
Add CORS middleware: https://fastapi.tiangolo.com/tutorial/cors/#use-corsmiddleware
As when frontend calls backend API, if CORS is not enabled it gives errors. 
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed, "*" allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def service_health():
    return {"Status: Root server healthy"}

@app.get("/api/getUserData")
async def get_user_data(username: str, age: int):
    # Mock data or fetch data from database
    user_data = {
        "username": username,
        "age": age,
        "details": "This is mock user data"
    }
    return user_data
