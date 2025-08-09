#!/usr/bin/python3
"""Initializes the state of the user"""
from models.base_model import BaseModel


class State(BaseModel):
    """Creates an instance of the state.

       Args:
            name: Name of the state -> public attribute
    """
    name = ""
