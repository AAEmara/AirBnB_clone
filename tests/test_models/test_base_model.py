"""Module for Unittesting the BaseModel Class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Testing the BaseModel Class."""
    def test_attr(self):
        """Testing attributes datatypes."""
        inst_1 = BaseModel()
        self.assertEqual(type(inst_1.id), str)
        self.assertEqual(type(inst_1.created_at), datetime)
        self.assertEqual(type(inst_1.updated_at), datetime)

    def test_save(self):
        """Testing save method."""
        inst_2 = BaseModel()
        self.assertEqual(inst_2.created_at, inst_2.updated_at)
        inst_2.save()
        self.assertNotEqual(inst_2.created_at, inst_2.updated_at)

    def test_to_dict(self):
        """Tasting to_dict method."""
        inst_3 = BaseModel()
        created_at_bef = inst_3.created_at
        updated_at_bef = inst_3.updated_at
        keys = list(inst_3.__dict__)
        self.assertNotIn("__class__", keys)
        dict_return = inst_3.to_dict()
        created_at_aft = inst_3.created_at
        updated_at_aft = inst_3.updated_at
        keys_update = list(inst_3.__dict__)
        self.assertIn("__class__", keys_update)
        self.assertNotEqual(created_at_bef, created_at_aft)
        self.assertNotEqual(updated_at_bef, updated_at_aft)
        self.assertEqual(type(created_at_aft), str)
        self.assertEqual(type(updated_at_aft), str)
