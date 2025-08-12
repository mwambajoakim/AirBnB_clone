#!/usr/bin/python3
"""Test the class Amenity"""
import unittest
import time
from uuid import UUID
frm models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up instance of Amenity"""
        self.my_amenity = Amenity()
