#!/usr/bin/python3
""" base_model """

import models
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ instantiate new base model object
            either using values provide using Kwags
            or without kwargs
        """

        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at" or key == "updated_at":
                    d = datetime.strptime(kwargs[key], t_format)
                    self.__dict__[key] = d
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ __str__ """
        c_name = self.__class__.__name__
        id = self.id
        dict = self.__dict__
        return ("[{}] ({}) {}".format(c_name, id, dict))

    def save(self):
        """ save """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary representation of a Rectangle."""
        # we can use this or
        # t_format = "%Y-%m-%dT%H:%M:%S.%f"
        # return {
        #     "id": self.id,
        #     "created_at": self.created_at.isoformat(),
        #     "updated_at": self.updated_at.isoformat(),
        #     "my_number": self.my_number,
        #     "name": self.name,
        #     "__class__": self.__class__.__name__
        # }
        # limitation of the above is if my_number or name is not set
        # then accessing them in later stages will raise error
        temp_dict = self.__dict__.copy()
        temp_dict["created_at"] = temp_dict["created_at"].isoformat()
        temp_dict["updated_at"] = temp_dict["updated_at"].isoformat()
        temp_dict["__class__"] = self.__class__.__name__
        return temp_dict
