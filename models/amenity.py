#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.place import place_amenity
#import models


class Amenity(BaseModel, Base):
    """This is the class for Amenity """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    place_amenities = relationship(
        "Place",
        secondary="place_amenity",
        viewonly=False,
        back_populates="amenities",
    )
