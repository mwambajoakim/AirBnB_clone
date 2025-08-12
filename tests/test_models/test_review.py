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

    def test_to_dict(self):
        my_dict = self.my_review.to_dict()
        created_iso = self.my_review.created_at.isoformat()
        updated_iso = self.my_review.updated_at.isoformat()

        self.assertEqual(self.my_review.id, my_dict["id"])
        self.assertEqual(created_iso, my_dict["created_at"])
        self.assertEqual(updated_iso, my_dict["updated_at"])
