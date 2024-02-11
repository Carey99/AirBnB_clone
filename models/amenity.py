#!/usr/bin/python3
"""Defines the amenity model"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The Amenity Model"""
    name: str = ""
