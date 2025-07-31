#!/usr/bin/python3
"""Serializes and deserializes to and from JSON files"""
import json


class FileStorage:
    """Serializes instances to JSON files and deserializes
    JSON files to instances
    """
    def __init__(self):
        self.__file_path = f"{__name__}.json"
        self.__objects = {}

    def all(self):
        """Returns all the objects in dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects, obj with key class name.id

           Args:
                obj: A BaseModel object
        """
        self.__objects = {
           __class__.__name__.id: obj
            }

    def save(self):
        """Serializes objects to filename, __file_path
        """
        with open(self.__file_path, 'a', encoding=UTF-8) as filename:
            filename.dump(self.__objects)
