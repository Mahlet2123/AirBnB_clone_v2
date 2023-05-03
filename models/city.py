#!/usr/bin/python3
""" User module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv


class City(BaseModel, Base):
    """class City that inherits from BaseModel"""

    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(128), nullable=False)

    places = relationship('Place', backref='cities', cascade='all, delete')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        state_id = ""
        name = ""


