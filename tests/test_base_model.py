#!/usr/bin/python3
"""Tests for the BaseModel"""
from models.base_model import BaseModel
import unittest
import datetime
import time
from uuid import UUID


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Sets up BaseModel"""
        self.my_model = BaseModel()
        self.my_model.name = "First Model"
        self.my_model.number = 100
        created_at = self.my_model.created_at
        updated_at = self.my_model.updated_at
        old_save = self.my_model.save()

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

    def test_save(self):
        """Tests the save method in BaseModel"""
        old_update = self.my_model.updated_at
        time.sleep(0.30)
        self.my_model.save()
        new_update = self.my_model.updated_at
        self.assertNotEqual(old_update, new_update)

    def test_ID(self):
        """Tests the automated ID"""
        self.assertTrue(hasattr(self.my_model, "id"))
        self.assertIsInstance(self.my_model.id, str)
        try:
            UUID(self.my_model.id)
            is_valid_uuid = True
        except ValueError:
            is_valid_uuid = False

        self.assertTrue(is_valid_uuid)

    def test_created_at(self):
        """Tests created_at attribute"""
        self.assertTrue(hasattr(self.my_model, "created_at"))
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)

    def test_updated_at(self):
        """Tests the updated_at attribute"""
        self.assertTrue(hasattr(self.my_model, "updated_at"))
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        old_update = self.my_model.updated_at
        time.sleep(0.30)
        self.my_model.save()
        new_update = self.my_model.updated_at

        self.assertNotEqual(old_update, new_update)
        self.assertGreater(new_update, old_update)

    def test_to_dict(self):
        """Tests the to_dict method"""
        my_dict = self.my_model.to_dict()

        self.assertEqual(self.my_model.id, my_dict["id"])
        self.assertEqual(self.my_model.created_at.isoformat(), my_dict["created_at"])
        self.assertEqual(self.my_model.updated_at.isoformat(), my_dict["updated_at"])
        self.assertEqual("BaseModel", my_dict["__class__"])
