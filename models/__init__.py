#!/usr/bin/python3
"""
Imports 'file_storage.py'
Creates a variable 'storage'
Calls reload() on 'storage' variable
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

from models.user import User
from models.base_model import BaseModel
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
    }
