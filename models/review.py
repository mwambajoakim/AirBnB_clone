#!/usr/bin/python3
"""Initializes the review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Creates an instance of Review class.

       Args:
            place_id: ID of the place(Will be be Place.id).
            user_id: ID of the user(Will be User.id).
            text: The review from the user.
    """
    place_id = ""
    user_id = ""
    text = ""
