#!/usr/bin/python3
"""Unit test Amenity"""
import unittest
import pep8
import os
from models.place import Place
from models.engine.file_storage import FileStorage


class Test(unittest.TestCase):
    """test"""

    def setUp(self):
        """set the class"""
        self.test_class = Place()

    def test_doc(self):
        """test the documentation """
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def test_permissions(self):
        """Test Permissions of file"""

        r = os.access('models/place.py', os.R_OK)
        self.assertTrue(r, "Read permissions")
        w = os.access('models/place.py', os.W_OK)
        self.assertTrue(w, "Write permissions")
        e = os.access('models/place.py', os.X_OK)
        self.assertTrue(e, "Execute permissions")

    def test_dict(self):
        """test the dict"""
        dict_test = self.test_class.to_dict()
        self.assertIsInstance(dict_test["created_at"], str)
        self.assertIsInstance(dict_test["updated_at"], str)
        self.assertIsInstance(dict_test["city_id"], str)
        self.assertIsInstance(dict_test["id"], str)
        self.assertIsInstance(dict_test["user_id"], str)
        self.assertIsInstance(dict_test["name"], str)
        self.assertIsInstance(dict_test["description"], str)
        self.assertIsInstance(dict_test["number_rooms"], int)
        self.assertIsInstance(dict_test["number_bathrooms"], int)
        self.assertIsInstance(dict_test["max_guest"], int)
        self.assertIsInstance(dict_test["price_by_night"], int)
        self.assertIsInstance(dict_test["latitude"], float)
        self.assertIsInstance(dict_test["longitude"], float)
        self.assertIsInstance(dict_test["amenity_ids"], list)

    def test_instance(self):
        """ check if amenity_1 is instance of Amenity """
        self.assertIsInstance(self.test_class, Place)
