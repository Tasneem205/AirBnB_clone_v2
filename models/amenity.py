#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
# from models.place import place_amenity
from models import storage_t

class Amenity(BaseModel, Base):
    if storage_t == "db":
        __tablename__ = 'amenities'
        name = Column("name", String(128), nullable=False)
        # place_amenities = relationship('Place', secondary='place_amenity', back_populates='amenities')
    else:
        name = ""
