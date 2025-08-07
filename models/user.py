#!/usr/bin/python3
"""Creates a new user"""
from models.base_model import BaseModel


class User(BaseModel):
    first_name = ""
    last_name = ""
    email = ""
    password = ""
