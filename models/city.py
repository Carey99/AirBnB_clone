#!/usr/bin/python3
"""Defines city model"""
from models.base_model import BaseModel


class City(BaseModel):
    """The City Model"""
    name: str = ""
    state_id: str = ""
