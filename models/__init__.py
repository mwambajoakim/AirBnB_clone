#!/usr/bin/python3
"""
Imports 'file_storage.py'
Creates a variable 'storage'
Calls reload() on 'storage' variable
"""
from . import engine
FileStorage = __import__("file_storage").FileStorage


storage = FileStorage()
storage.reload()
