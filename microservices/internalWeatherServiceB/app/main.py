from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import os
from app.db import init_db
from app.routes.weather_routes import router as weather_router

app = FastAPI()

if os.getenv("DOCKER_COMPOSE_MODE", "None") == 'True':
    init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def server_health_check():
    return {"Status": "Internal Weather Service Server healthy!"}

app.include_router(weather_router, prefix="/api", tags=["weather_api_routes"]) # Prefix /api adds prefix to endpoints, so say our /v1 endpoint would actually be /api/v1.
