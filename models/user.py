#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base_model import BaseModel, Base
from models import storage_t


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if storage_t == "db":
        __tablename__ = 'users'
        email = Column("email", String(128), nullable=False)
        password = Column("password", String(128), nullable=False)
        first_name = Column("first_name", String(128))
        last_name = Column("last_name", String(128))
        # Assuming other attributes are already defined
        reviews = relationship('Review', back_populates='user', cascade='all, delete')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        reviews = []
