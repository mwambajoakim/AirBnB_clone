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
        slef.my_city.name = "Nairobi"

