#!/usr/bin/python3
"""All tests for class FileStorage are herein"""
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.Testcase):
    def setUp(self):
        store = FileStorage()

    

