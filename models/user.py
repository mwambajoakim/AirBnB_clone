#!/usr/bin/python3
"""Creates a new user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Instantiates a user

       Args:
            first_name: First name of the user.
            last_name: Last name of the user.
            email: Email of the user.
            password: Password of the user.
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
