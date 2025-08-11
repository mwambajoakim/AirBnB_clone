#!/usr/bin/python3
"""All tests for class FileStorage are herein"""
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.store = FileStorage()

    def test_all(self):
        """Test the all() method"""
        self.assertTrue(self.store.all())

