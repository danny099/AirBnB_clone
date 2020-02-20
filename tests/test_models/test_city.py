#!/usr/bin/python3
"""Unit test Amenity"""
import unittest
import pep8
import os
from models.city import City
from models.engine.file_storage import FileStorage


class Test(unittest.TestCase):
    """test"""

    def setUp(self):
        """set the class"""
        self.test_class = City()

    def test_doc(self):
        """test the documentation """
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def test_name(self):
        """test the name"""
        name_test = 'Bogota'
        self.test_class.name = name_test
        self.assertEqual(self.test_class.name, name_test)

    def test_dict(self):
        """test the dict"""
        dict_test = self.test_class.to_dict()
        self.assertIsInstance(dict_test["created_at"], str)
        self.assertIsInstance(dict_test["updated_at"], str)
        self.assertIsInstance(dict_test["state_id"], str)
        self.assertIsInstance(dict_test["id"], str)

    def test_instance(self):
        """ check if amenity_1 is instance of Amenity """
        self.assertIsInstance(self.test_class, City)
