#!/usr/bin/python3
"""Defines review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review Model"""

    place_id: str = ""
    user_id: str = ""
    text: str = ""
