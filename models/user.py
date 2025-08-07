#!/usr/bin/python3
"""Creates a new user"""
from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self):
        """Initializes a new user"""
        self.firs_name = ""
        self.last_name = ""
        self.email = ""
        self.password = ""
