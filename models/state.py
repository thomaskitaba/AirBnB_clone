#!/usr/bin/python3
"""State subclass of BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """ State sub classes of BaseModel """

    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation for the State class"""
        super().__init__(*args, **kwargs)
