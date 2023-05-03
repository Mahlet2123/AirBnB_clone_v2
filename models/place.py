#!/usr/bin/python3
""" Place module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv


class Place(BaseModel, Base):
    """class Place that inherits from BaseModel"""

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id', ondelete="CASCADE"), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    reviews = relationship('Review', backref='place', cascade='all, delete')

    
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        def reviews(self):
            """  getter attribute reviews that returns the list of Review
            instances with place_id equals to the current Place.id """
            from models import storage
            from models import Place

            review_list = []
            for place_key, place_obj in storage.all(Place).items():
                if place_obj.place.id == self.id:
                    review_list.append(place_obj)
            return review_list

