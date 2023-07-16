#!/usr/bin/python3
""" User class: sub class of base_model """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from BaseModel: """

    email = ""  # string - empty string
    password = ""  # string - empty string
    first_name = ""  # string - empty string
    last_name = ""  # string - empty string

    def __init__(self, *args, **kwargs):
        """Instantiation for the User class"""
        super().__init__(*args, **kwargs)
