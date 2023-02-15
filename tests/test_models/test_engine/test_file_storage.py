#!/usr/bin/python3
'''unitttest for the FileStorage class'''

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    '''sets up instanses of the FileStorage and the BaseModel classes'''
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        '''this teardown menthod ensures that any files created during the instance 
        creation is deleted after the test'''
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        '''this method tests if the instances created are indeed
        objects and if they it is initially empty'''
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertEqual(len(all_objs), 0)

    def test_new(self):
        '''tests the creation of a new instance and checks if it is added to __object'''
        self.storage.new(self.model)
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)

    def test_save_reload(self):
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertEqual(len(all_objs), 1)
        key = self.model.__class__.__name__ + "." + self.model.id
        self.assertIsNotNone(all_objs[key])
        self.assertIsInstance(all_objs[key], BaseModel)


if __name__ == "__main__":
    unittest.main()
