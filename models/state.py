#!/usr/bin/python3
""" User module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """class State that inherits from BaseModel"""

    __tablename__ = 'states'
    name = Column(String(60), nullable=False)

    cities = relationship('City', backref='state', cascade='all, delete')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        name = ""

        @property
        def cities(self):
            """  getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id """
            from models import storage
            from models import City

            city_list = []
            for city_key, city_obj in storage.all(City).items():
                if city_obj.state_id == self.id:
                    city_list.append(city_obj)
            return city_list
