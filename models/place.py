#!/usr/bin/python3
"""Initializes the place of the user."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Creates an instance of the place.

       Args:
            city_id: ID of the city.
            user_id: ID of the user.
            name: Name of the place.
            description: Description of the place.
            number_rooms: Number of rooms.
            number_bathrooms: Number of bathrooms.
            max_guest: Maximum number of guests.
            price_by_night: Price of place per night.
            latitude: Latitude of the place.
            longitude: Longitude of the place.
            amenity_ids: IDs of the amenity.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
