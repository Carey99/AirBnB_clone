#!/usr/bin/python3
"""The basemodel where other classes inherits from"""
import sys
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attribute for other classes"""
    def __init__(self):
        """Public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def update(self, **kwargs):
        """Assign datetime when instance is created and will be updated"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.update_at = datetime.now()

    def save(self):
        """Updates the updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all key/values of instances"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Should print [<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
        print("\n\n")


if __name__ == "__main__":
    pass
