#!/usr/bin/python3
"""Defines the base model for use with other classes"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes

    Args:
           id: Id of the instance, automatically generated.
           created_at: Assigns current datetime when instance is created .
           updated_at: Assigns current datetime when instance is updated.
    """
    def __init__(self, *args, **kwargs):
        """Initializes the attributes of the class

        Args:
            *args: Multiple arguments that can be
                   used to set an instance of BaseModel.
            **kwargs: Multiple key-worded arguments
                      that can be used to set an instance of BaseModel.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    str_format = "%Y-%m-%dT%H:%M:%S.%f"
                    dateformat = datetime.strptime(value, str_format)
                    setattr(self, key, dateformat)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new()

    def __str__(self):
        """Returns a string of the class name, its id and dict
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the update_at attribute with the current time
        """
        self.updated_at = datetime.now()
        storage.save()
        return self.updated_at

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        new_dict = {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
            }
        return new_dict
