#!/usr/bin/python3
"""Test the class Place"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Sets up an instance of Place"""
        self.my_place = Place()
        
