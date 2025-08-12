#!/usr/bin/python3
"""Test the class City"""
import unittest
import time
import uuid
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up an instance of City"""
        self.my_city = City()
        self.my_city.name = "Nairobi"

    def test_issubclass(self):
        """Asserts City inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_created_at(self):
        """Tests the instance has an attribute 'created_at'"""
        self.assertTrue(hasattr(self.my_city, "created_at"))
