#!/usr/bin/python3
"""Initializes the city of user"""
from models.base_model import BaseModel


class City(BaseModel):
    """Creates an instance of the user's city.

       Args:
            state_id: ID of the state.
            name: Name of the city.
    """
    state_id = ""
    name = ""
