#!/usr/bin/python3
"""
    Serializes instance to json and deserializes to instances
"""
import json
from json.decoder import JSONDecodeError
from models.base_model import BaseModel
import os


class FileStorage:
    __file_path: str = "file.json"
    __objects: dict = {}

    def __init__(self):
        """constructor"""
        pass

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key..."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes to json file"""
        serialized = {
            key: val.to_dict()
            for key, val in self.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(serialized))

    def reload(self):
        """deserializes json files"""
        try:
            deserialized = {}
            with open(FileStorage.__file_path, "r") as f:
                deserialized = json.loads(f.read())
            FileStorage.__objects = {
                key:
                    eval(obj["__class__"])(**obj)
                    for key, obj in deserialized.items()}
        except (FileNotFoundError, JSONDecodeError):
            pass
