#!/usr/bin/python3
"""Unit test Amenity"""
import unittest
import json
import pep8
from os import path
from models.city import City
import models
import os


class TestBase(unittest.TestCase):
    """ Test all of i think """

    def setUp(self):
        """ Set a variable """
        self.test_class = City

    def TestModels(self):
        """Test model name"""
        self.assertIsNotNone(
            models.city.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(City.__doc__, "No docstring in the class")

    def TestPermission(self):
        r = os.access('models/city.py', os.R_OK)
        self.assertTrue(r, "Read permissions")
        w = os.access('models/city.py', os.W_OK)
        self.assertTrue(w, "Write permissions")
        e = os.access('models/city.py', os.X_OK)
        self.assertTrue(e, "Execute permissions")

    def test_type(self):
        """Test type of class"""

        self.assertEqual(
            str(type(self.file_storage)),
            "<class 'models.city.City'>")
        self.assertIsInstance(self.file_storage, City)


if __name__ == '__main__':
    unittest.main()
