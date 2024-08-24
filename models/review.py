#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import BaseModel, Base
from .user import User
from models import storage_t


class Review(BaseModel, Base):
    if storage_t == "db":
        __tablename__ = 'reviews'
        text = Column("text", String(1024), nullable=False)
        place_id = Column("place_id", String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column("user_id", String(60), ForeignKey('users.id'), nullable=False)
        user = relationship("User", back_populates="reviews")
    else:
        text = ""
        place_id = ""
        user_id = ""
        user = ""
