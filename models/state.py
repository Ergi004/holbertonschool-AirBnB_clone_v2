#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import Base
from sqlalchemy import Column, Integer, \
    String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128),
                  nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            from models.city import City
            from models import storage

            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]
