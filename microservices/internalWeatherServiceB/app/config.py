from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    REDIS_HOST: str
    REDIS_PORT: str
    MONGO_HOST: str
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_PORT: str
    MONGO_DB: str
    DOCKER_COMPOSE_MODE: str


    class Config:
        env_file = ".env"

# Note we could import env file variables via:
# from dotenv import load_dotenv
# import os
# load_dotenv()  # Load the .env file
# POSTGRES_USER = os.getenv('POSTGRES_USER')
# POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
# Or use Pydantic BaseSettings which we used here

settings = Settings()
