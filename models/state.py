#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref=backref("state", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True,
    )

    @property
    def cities(self):
        """returns list of City instances with state_id"""
        from models import storage
        from models import City

        for k, v in storage.all(City).items():
            if v.state_id == self.state_id:
                return v

    name = ""
