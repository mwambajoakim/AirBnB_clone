#!/usr/bin/python3
"""Test the class Place"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Sets up an instance of Place"""
        self.my_place = Place()
        self.my_place.name = "Duwaa"

    def test_issubclass(self):
        """Test instance is subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_name(self):
        """Assert name exists"""
        self.assertEqual(self.my_place.name, "Duwaa")

    def test_created_at(self):
        """Test the instance 'my_place has the attribute
        'created_at'"""
        self.assertTrue(hasattr(self.my_place, "created_at"))

    def test_updated_at(self):
        """Test the instance 'my_place has the attribute
        'updated_at'"""
        self.assertTrue(hasattr(self.my_place, "updated_at"))

    def test_to_dict(self):
        """Test the method 'to_dict' is accurate"""
        my_dict = self.my_place.to_dict()
        created_iso = self.my_place.created_at.isoformat()
        updated_iso = self.my_place.updated_at.isoformat()

        self.assertEqual(self.my_place.id, my_dict["id"])
        self.assertEqual(created_iso, my_dict["created_at"])
        self.assertEqual(updated_iso, my_dict["updated_at"])

    def test_kwargs(self):
        """Instantiate a new instance with current instance dict"""
        my_dict = self.my_place.to_dict()
        self.new_place = Place(**my_dict)

        self.assertEqual(self.new_place.id, self.my_place.id)
