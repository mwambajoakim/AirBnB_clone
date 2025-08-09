#!/usr/bin/python3
"""Serializes and deserializes to and from JSON files"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes instances to JSON files and deserializes
    JSON files to instances
    """
    __file_path = f"{__name__}.json"
    __objects = {}
    

    def all(self):
        """Returns all the objects in dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects, obj with key class name.id

           Args:
                obj: A BaseModel object
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes objects to filename, __file_path
        """
        json_obj = {}
        for key, obj in self.__objects.items():
            json_obj[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as filename:
            json.dump(json_obj, filename)

    def reload(self):
        """Deserializes objects from filename __file_path to __objects
        """
        classes = {
        "BaseModel": BaseModel,
        "User": User
    }
        try:
            with open(self.__file_path, encoding="UTF-8") as filename:
                json_data  = json.load(filename)

            for key, obj_dict in json_data.items():
                class_name = obj_dict["__class__"]
                if class_name in classes:
                    self.__objects[key] = classes[class_name](**obj_dict)
        except Exception:
            pass
