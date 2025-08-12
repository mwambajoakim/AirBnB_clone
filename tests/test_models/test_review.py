#!/usr/bin/python3
"""Test the class Review"""
from models.base_model import BaseModel
from models.review import Review
import unittest
import datetime


class TestReview(unittest.TestCase):
    def setUp(self):
        self.my_review = Review()
