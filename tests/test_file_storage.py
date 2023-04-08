#!/usr/bin/python3

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def setUp(self):
        """Set up the test environment"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.save()

    def tearDown(self):
        """Tear down the test environment"""
        if os.path.isfile('file.json'):
            os.remove('file.json')

    def test_all(self):
        """Test the all method"""
        models = self.storage.all()
        self.assertIsInstance(models, dict)
        self.assertIn('BaseModel.{}'.format(self.model.id), models.keys())

    def test_new(self):
        """Test the new method"""
        models = BaseModel()
        self.storage.new(models)
        objs = self.storage.all()
        self.assertIn('BaseModel.{}'.format(models.id), objs)

    def test_save(self):
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open('file.json', 'r') as f:
            content = f.read()
            self.assertIn('BaseModel.{}'.format(model.id), content)

    def test_reload(self):
        self.storage.save()
        self.storage.reload()
        models = self.storage.all()
        self.assertIsInstance(models, dict)
        self.assertIn('BaseModel.{}'.format(self.model.id), models.keys())


if __name__ == '__main__':
    unittest.main()
