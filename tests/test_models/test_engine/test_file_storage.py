import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertEqual(len(all_objs), 0)

    def test_new(self):
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
