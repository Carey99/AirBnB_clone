#!/usr/bin/python3
"""
    Serializes instance to json and deserializes to instances
"""
import json
import os


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key..."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes to json file"""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """deserializes json files"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    module = __import__('models.' + class_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    self.__objects[key] = class_(**value)
