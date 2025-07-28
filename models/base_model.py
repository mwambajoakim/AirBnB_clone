#!/usr/bin/python3
"""Defines the base model for use with other classes"""
import uuid
import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes

    Args:
           id: Id of the instance, automatically generated.
           created_at: Assigns current datetime when instance is created .
           updated_at: Assigns current datetime when instance is updated.
    """
    def __init__(self):
        """Initializes the attributes of the class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string of the class name, its id and dict
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the update_at attribute with the current time
        """
        self.updated_at = datetime.datetime.now()
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
