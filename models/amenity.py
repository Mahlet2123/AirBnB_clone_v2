#!/usr/bin/python3
""" User module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """class Amenity that inherits from BaseModel"""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    place_amenities = relationship(
        "Place", secondary="place_amenity", viewonly=False, back_populates="amenities"
    )
