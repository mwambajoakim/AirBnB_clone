#!/usr/bin/python3
"""Initializes the amenity of the user."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Creates an instance of the user's amenity.

       Args:
            name: Name of the amenity.
    """
    name = ""
