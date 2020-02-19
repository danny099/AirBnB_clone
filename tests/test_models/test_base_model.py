#!/usr/bin/python3
"""Unit test Base Model"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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
        name_test = 'Holberton Test'
        self.test_class.name = name_test
        self.assertEqual(self.test_class.name, 'Holberton')
        self.test_class.my_number = 55
        self.assertEqual(self.test_class.my_number, 55)
        dict_test = self.test_class.to_dict()
        self.assertIsInstance(dict_test["created_at"], str)
        self.assertIsInstance(dict_test["updated_at"], str)
        self.assertIsInstance(dict_test["my_number"], int)
        self.assertIsInstance(dict_test["id"], str)
