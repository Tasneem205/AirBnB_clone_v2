#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base_model import BaseModel, Base
from models import storage_t

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column("state_id", String(60), ForeignKey('states.id'), nullable=False)
        name = Column("name", String(128), nullable=False)
        places = relationship(
                 'Place', backref='cities', cascade='all, delete, delete-orphan')
    else:
        state_id = ""
        name = ""
