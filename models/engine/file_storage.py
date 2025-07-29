#!/usr/bin/python3
"""Serializes and deserializes to and from JSON files"""


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

    def 
