#!/usr/bin/python3
import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_update(self):
        model = BaseModel()
        model.update(name='updated_name', age=25)
        self.assertEqual(model.name, 'updated_name')
        self.assertEqual(model.age, 25)

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertEqual(model_dict['id'], model.id)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_str(self):
        model = BaseModel()
        expected_output = f"[BaseModel] ({model.id}) {model.__dict__}\n"
        self.assertEqual(str(model), expected_output)


if __name__ == '__main__':
    unittest.main()
