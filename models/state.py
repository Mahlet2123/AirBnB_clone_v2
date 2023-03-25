#!/usr/bin/python3
""" User module"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel):
    """class State that inherits from BaseModel"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all,delete,delete-orphan",
        backref=backref("state", cascade="all,delete"),
    )

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """returns list of City instances with state_id"""
            from models import storage
            from models import City

            for k, v in storage.all(City).items():
                if v.state_id == self.state_id:
                    return v
    # name = ""
