#!/usr/bin/python3
"""
    Serializes instance to json and deserializes to instances
"""
import json
from json.decoder import JSONDecodeError
from models.engine.error import *
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class FileStorage:
    __file_path: str = "file.json"
    __objects: dict = {}
    models = (
        "BaseModel",
        "User", "City", "State", "Place",
        "Amenity", "Review"
    )

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

    def find_by_id(self, model, obj_id):
        """Find and return an element of model by its id"""
        f = FileStorage
        if model not in f.models:
            raise ModelNotFoundError(model)

        key = model + "." + obj_id
        if key not in f.__objects:
            raise InstanceNotFoundError(obj_id, model)

        return f.__objects[key]

    def delete_by_id(self, model, obj_id):
        """Find and return an element of model by its id"""
        f = FileStorage
        if model not in f.models:
            raise ModelNotFoundError(model)

        key = model + "." + obj_id
        if key not in f.__objects:
            raise InstanceNotFoundError(obj_id, model)

        del f.__objects[key]
        self.save()

    def find_all(self, model=""):
        """Find all instances or instances of model"""
        if model and model not in FileStorage.models:
            raise ModelNotFoundError(model)
        results = []
        for key, val in FileStorage.__objects.items():
            if key.startswith(model):
                results.append(str(val))
        return results

    def update_one(self, model, iid, field, value):
        """Updates an instance"""
        f = FileStorage
        if model not in f.models:
            raise ModelNotFoundError(model)

        key = model + "." + iid
        if key not in f.__objects:
            raise InstanceNotFoundError(iid, model)
        if field in ("id", "updated_at", "created_at"):
            return
        inst = f.__objects[key]
        try:
            vtype = type(inst.__dict__[field])
            inst.__dict__[field] = vtype(value)
        except KeyError:
            inst.__dict__[field] = value
        finally:
            inst.updated_at = datetime.utcnow()
            self.save()
