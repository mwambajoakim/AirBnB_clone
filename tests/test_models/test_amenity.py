#!/usr/bin/python3
"""Test the class Amenity"""
import unittest
import time
from uuid import UUID
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up instance of Amenity"""
        self.my_amenity = Amenity()

    def test_issubclass(self):
        """Test Amenity inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_name(self):
        """Test the instance has attribute 'name'"""
        self.assertTrue(hasattr(self.my_amenity, "name"))

    def test_created_at(self):
        """Test instance has attribute 'created_at'"""
        self.assertTrue(hasattr(self.my_amenity, "created_at"))

    
