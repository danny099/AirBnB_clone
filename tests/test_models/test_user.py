#!/usr/bin/python3
'''Unit test User class'''
import unittest
import json
import pep8
from os import path
from models.user import User
import models
import os


class TestBase(unittest.TestCase):
    """ Test all of i think """

    def setUp(self):
        """ Set a variable """
        self.test_class = User

    def TestModels(self):
        """Test model name"""
        self.assertIsNotNone(
            models.user.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(User.__doc__, "No docstring in the class")

    def TestPermission(self):
        r = os.access('models/user.py', os.R_OK)
        self.assertTrue(r, "Read permissions")
        w = os.access('models/user.py', os.W_OK)
        self.assertTrue(w, "Write permissions")
        e = os.access('models/user.py', os.X_OK)
        self.assertTrue(e, "Execute permissions")

    def test_type(self):
        """Test type of class"""

        self.assertEqual(
            str(type(self.file_storage)),
            "<class 'models.user.User'>")
        self.assertIsInstance(self.file_storage, User)


if __name__ == '__main__':
    unittest.main()
