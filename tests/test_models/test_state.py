#!/usr/bin/python3
"""Test the class State"""
from models.state import State
from models.base_model import BaseModel
import datetime
import unittest


class TestState(unittest.TestCase):
    def setUp(self):
        """Sets up a state for testing"""
        self.my_state = State()
        self.my_state.name = "Nairobi"

    def test_state_name(self):
        """Asserts if the name for state is stored"""
        self.assertEqual(self.my_state.name, "Nairobi")

    def test_created_at(self):
        """Checks if State has the attribute 'created_at'"""
        self.assertTrue(hasattr(self.my_state, "created_at"))

    def test_updated_at(self):
        """Checks if State has the attribute 'updated_at'"""
        self.assertTrue(hasattr(self.my_state, "updated_at"))

    def test_kwargs(self):
        """Tests if it is possible to initialize another
        instance using the dict of another instance"""
        my_dict = self.my_state.to_dict()
        self.my_new_state = State(**my_dict)
        self.assertEqual(self.my_state.id, self.my_new_state.id)

    def test_to_dict(self):
        """Tests if the dict is accurate"""
        my_dict = self.my_state.to_dict()
        created_iso = self.my_state.created_at.isoformat()
        updated_iso = self.my_state.updated_at.isoformat()

        self.assertEqual(self.my_state.id, my_dict["id"])
        self.assertEqual(created_iso, my_dict["created_at"])
        self.assertEqual(updated_iso, my_dict["updated_at"])

    def test_subclass(self):
        """Checks if State inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))
