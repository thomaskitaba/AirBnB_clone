#!/usr/bin/python3
""" City sub classes of BaseModel """

from models.base_model import BaseModel


class City(BaseModel):
    """ City """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation for the City class"""
        super().__init__(*args, **kwargs)
