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
