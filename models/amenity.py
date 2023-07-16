#!/usr/bin/python3
""" Amenity sub classes of BaseModel """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity """

    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation for the amenity class"""
        super().__init__(*args, **kwargs)
