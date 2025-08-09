#!/usr/bin/python3
"""
Imports 'file_storage.py'
Creates a variable 'storage'
Calls reload() on 'storage' variable
"""
from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()
classes = {
    "BaseModel": BaseModel,
    "User": User
    }
