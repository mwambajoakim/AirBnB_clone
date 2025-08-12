#!/usr/bin/python3
"""Test the class Review"""
from models.base_model import BaseModel
from models.review import Review
import unittest
import datetime


class TestReview(unittest.TestCase):
    def setUp(self):
        """Sets up an instance of Review"""
        self.my_review = Review()

    def test_issubclass(self):
        """Tests if Review inherits from
        BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_created_at(self):
        """Test 'created_at' attribute exists"""
        self.assertTrue(hasattr(self.my_review, "created_at"))

    def test_updated_at(self):
        """Test 'updated_at' attribute exists"""
        self.assertTrue(hasattr(self.my_review, "updated_at"))
