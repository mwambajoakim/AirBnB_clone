#!/usr/bin/python3
"""Test the class User"""
from models.user import User
import unittest
import datetime


class TestUser(unittest.TestCase):
    def setUp(self):
        self.my_user = User()
        self.my_user.first_name = "Joe"
        self.my_user.last_name = "Log"
        self.my_user.email = "joelog@email.com"
        self.my_user.password = "jl1234"
        created_at = self.my_user.created_at
        updated_at = self.my_user.updated_at

    def test_user_fname(self):
        self.assertEqual(self.my_user.first_name, "Joe")

    def test_user_lname(self):
        self.assertEqual(self.my_user.last_name, "Log")

    def test_user_email(self):
        self.assertEqual(self.my_user.email, "joelog@email.com")

    def test_user_pass(self):
        self.assertEqual(self.my_user.password, "jl1234")

    def test_created_at(self):
        self.assertTrue(hasattr(self.my_user, "created_at"))
        self.assertTrue(isinstance(self.my_user, User))

    def test_updated_at(self):
        self.assertTrue(hasattr(self.my_user, "updated_at"))

    def test_to_dict(self):
        my_dict = self.my_user.to_dict()
        created_iso = self.my_user.created_at.isoformat()
        updated_iso = self.my_user.updated_at.isoformat()
        self.assertEqual(my_dict["id"], self.my_user.id)
        self.assertEqual(my_dict["created_at"], created_iso)
        self.assertEqual(my_dict["updated_at"], updated_iso)
