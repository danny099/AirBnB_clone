#!/usr/bin/python3
"""Unit test Base Model"""
import unittest
import json
import pep8
from os import path
from models.base_model import BaseModel
import models
import os


class Testpep8(unittest.TestCase):
    """Pep8 testing"""

    def test_pep8(self):
        msg = "Found code style errors (and warning)."
        style = pep8.StyleGuide(quiet=True)
        FileBase_Model = "models/base_model.py"
        FileBase_ModelTest = "tests/test_models/test_base_model.py"
        check = style.check_files([FileBase_Model, FileBase_ModelTest])
        self.assertEqual(check.total_errors, 0, msg)


class TestBase(unittest.TestCase):
    """ Test all of i think """

    def setUp(self):
        """ Set a variable """
        self.test_class = BaseModel

    def TestModels(self):
        """Test model name"""
        self.assertIsNotNone(
            models.base_model.__doc__,
            "No docstring in the module"
        )
        r = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(r, "Read permissions")
        w = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(w, "Write permissions")
        e = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(e, "Execute permissions")
        self.assertIsNotNone(BaseModel.__doc__, "No docstring in the class")
        self.test_class.name = 'Holberton'
        self.assertEqual(self.test_class.name, 'Holberton')
        self.test_class.my_number = 55
        self.assertEqual(self.test_class.my_number, 55)
        self.assertTrue(path.isfile('my_file.json'))
        model = self.test_class.to_dict()
        self.assertIsInstance(model["created_at"], str)
        self.assertIsInstance(model["updated_at"], str)
        self.assertIsInstance(model["my_number"], int)
        self.assertIsInstance(model["id"], str)


if __name__ == '__main__':
    unittest.main()
