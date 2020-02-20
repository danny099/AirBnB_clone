#!/usr/bin/python3
"""Unit test Base Model"""
import unittest
import json
import pep8
from os import path
from models.base_model import BaseModel
import models
import os


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
        self.assertIsNotNone(BaseModel.__doc__, "No docstring in the class")

    def TestPermission(self):
        r = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(r, "Read permissions")
        w = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(w, "Write permissions")
        e = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(e, "Execute permissions")

    def test_type(self):
        """Test type of class"""

        self.assertEqual(
            str(type(self.file_storage)),
            "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(self.file_storage, BaseModel)


if __name__ == '__main__':
    unittest.main()
