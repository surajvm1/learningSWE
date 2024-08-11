from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.db import Base

class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True)
    location = Column(String, index=True)
    temperature = Column(Integer)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
