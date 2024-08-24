#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from .base_model import BaseModel, Base
from models import storage_t


class State(BaseModel, Base):
    """ State class """
    if storage_t == "db":
        __tablename__ = 'states'
        name = Column("name", String(128), nullable=False)
    else:
        name = ""
