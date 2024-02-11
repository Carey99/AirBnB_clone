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
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of instances"""
        obj_dict = {**self.__dict__}
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        obj_dict['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return obj_dict

    @classmethod
    def all(cls):
        """Retrieve all current instances of cls"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """Get the number of all current instances of cls"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """Creates an Instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """Retrieve an instance"""
        return models.storage.find_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def destroy(cls, instance_id):
        """Deletes an instance"""
        return models.storage.delete_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def update(cls, instance_id, *args):
        """Updates an instance"""
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                cls.__name__,
                instance_id,
                *arg
            )
