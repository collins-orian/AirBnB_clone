from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    '''test BaseModel'''

    def setUp(self):
        self.base_modal = BaseModel()

    def test_kwargs(self):
        '''create a BaseModel instance with kwargs'''
        examp_kwargs = {'id': self.base_modal.id, 'created_at':
                        self.base_modal.created_at, 'updated_at': self.base_modal.updated_at}
        instance_test = BaseModel(**examp_kwargs)

        self.assertEqual(self.base_modal.id, instance_test.id)
        self.assertEqual(self.base_modal.created_at, instance_test.created_at)
        self.assertEqual(self.base_modal.updated_at, instance_test.updated_at)

    def test_id(self):
        self.assertIsInstance(self.base_modal.id, str)

    def test_to_dict(self):
        # Test that to_dict returns a dictionary
        self.assertIsInstance(self.base_model.to_dict(), dict)

        # Test that the dictionary has the correct keys and values
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)

    def test_save(self):
        # Test that calling save updates updated_at
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test___str__(self):
        expected_output = "[{}] ({}) {}".format(
            self.base_modal.__class__.__name__, self.base_modal.id, self.base_modal.__dict__)
        self.assertEqual(str(self.base_modal), expected_output)


if __name__ == "__main__":
    unittest.main()
