#!/usr/bin/python3
"""The basemodel where other classes inherits from"""
import sys
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Defines all common attribute for other classes"""
    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            return

        for key, val in kwargs.items():
            if key == '__class__':
                continue
            self.__dict__[key] = val
        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """override str representation of self"""
        fmt = "[{}] ({}) {}"
        return fmt.format(
                type(self).__name__,
                self.id,
                self.__dict__)

    def save(self):
        """Updates the updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of instances"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def update(self, **kwargs):
        """Assign datetime when instance is created and will be updated"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.update_at = datetime.now()
