#!/usr/bin/python3
""" User module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class User(BaseModel, Base):
    """class User that inherits from BaseModel"""

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', backref=backref("user", cascade="all,delete"))
    reviews = relationship('Place', backref=backref("review_user", cascade="all,delete"),)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        email = ""
        password = ""
        first_name = ""
        last_name = ""
