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

    def test_updated_at(self):
        self.assertTrue(hasattr(self.my_amenity, "updated_at"))

        old_update = self.my_amenity.updated_at
        time.sleep(0.70)
        self.my_amenity.save()
        new_update = self.my_amenity.updated_at

        self.assertLess(old_update, new_update)
        self.assertNotEqual(new_update, old_update)

    def test_ID(self):
        """Test the instance id"""
        self.assertTrue(hasattr(self.my_amenity, "id"))

        try:
            UUID(self.my_amenity.id)
            is_valid = True
        except ValueError:
            is_valid = False
        self.assertTrue(is_valid)

    
