#!/usr/bin/python3
"""Unit test Amenity"""
import unittest
import json
import pep8
from os import path
from models.place import Place
import models
import os


class TestBase(unittest.TestCase):
    """ Test all of i think """

    def setUp(self):
        """ Set a variable """
        self.test_class = Place

    def TestModels(self):
        """Test model name"""
        self.assertIsNotNone(
            models.place.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Place.__doc__, "No docstring in the class")

    def TestPermission(self):
        r = os.access('models/place.py', os.R_OK)
        self.assertTrue(r, "Read permissions")
        w = os.access('models/place.py', os.W_OK)
        self.assertTrue(w, "Write permissions")
        e = os.access('models/place.py', os.X_OK)
        self.assertTrue(e, "Execute permissions")

    def test_type(self):
        """Test type of class"""

        self.assertEqual(
            str(type(self.file_storage)),
            "<class 'models.place.Place'>")
        self.assertIsInstance(self.file_storage, Place)


if __name__ == '__main__':
    unittest.main()
