#!/usr/bin/python3
"""Test the class User"""
from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up an instance of 'User'"""
        self.my_user = User()
        self.my_user.first_name = "Joe"
        self.my_user.last_name = "Log"
        self.my_user.email = "joelog@email.com"
        self.my_user.password = "jl1234"

    def test_issubclass(self):
        """Assert 'User' inherits from 'BaseModel'"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_fname(self):
        """Check attribute 'first_name' exists"""
        self.assertTrue(hasattr(self.my_user, "first_name"))
        self.assertEqual(self.my_user.first_name, "Joe")

    def test_user_lname(self):
        """Check attribute 'last_name' exists"""
        self.assertTrue(hasattr(self.my_user, "last_name"))
        self.assertEqual(self.my_user.last_name, "Log")

    def test_user_email(self):
        """Check attribute 'email' exists"""
        self.assertTrue(hasattr(self.my_user, "email"))
        self.assertEqual(self.my_user.email, "joelog@email.com")

    def test_user_pass(self):
        """Check attribute 'password' exists"""
        self.assertTrue(hasattr(self.my_user, "password"))
        self.assertEqual(self.my_user.password, "jl1234")

    def test_created_at(self):
        """Check attribute 'created_at' exists"""
        self.assertTrue(hasattr(self.my_user, "created_at"))
        self.assertTrue(isinstance(self.my_user, User))

    def test_updated_at(self):
        """Check attribute 'updated_at' exists"""
        self.assertTrue(hasattr(self.my_user, "updated_at"))

    def test_to_dict(self):
        """Test the 'to_dict' method"""
        my_dict = self.my_user.to_dict()
        created_iso = self.my_user.created_at.isoformat()
        updated_iso = self.my_user.updated_at.isoformat()
        self.assertEqual(my_dict["id"], self.my_user.id)
        self.assertEqual(my_dict["created_at"], created_iso)
        self.assertEqual(my_dict["updated_at"], updated_iso)

    def test_kwargs(self):
        """Test instantiation by kwargs"""
        my_dict = self.my_user.to_dict()
        self.my_new_user = User(**my_dict)
        self.assertEqual(self.my_new_user.id, self.my_user.id)
