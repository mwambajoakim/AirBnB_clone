#!/usr/bin/python3
"""Tests for the BaseModel"""
from models.base_model import BaseModel
import unittest
import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Sets up BaseModel"""
        self.my_model = BaseModel()
        self.my_model.name = "First Model"
        self.my_model.number = 100

    def test_name(self):
        """Tests the name of instance"""
        self.assertEqual(self.my_model.name, 'First Model')

    def test_number(self):
        """Tests the number of instance"""
        self.assertEqual(self.my_model.number, 100)

    def test_str(self):
        """Tests the __str__ method"""
        expected_str = f"[BaseModel] ({self.my_model.id}) {self.my_model.__dict__}"
        self.assertEqual(str(self.my_model), expected_str)
