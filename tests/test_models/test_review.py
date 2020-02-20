#!/usr/bin/python3
"""Unit test Amenity"""
import unittest
import pep8
import os
from models.review import Review
from models.engine.file_storage import FileStorage


class Test(unittest.TestCase):
    """test"""

    def setUp(self):
        """set the class"""
        self.test_class = Review()

    def test_doc(self):
        """test the documentation """
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)

    def test_dict(self):
        """test the dict"""
        dict_test = self.test_class.to_dict()
        self.assertIsInstance(dict_test["created_at"], str)
        self.assertIsInstance(dict_test["updated_at"], str)
        self.assertIsInstance(dict_test["place_id"], str)
        self.assertIsInstance(dict_test["id"], str)
        self.assertIsInstance(dict_test["user_id"], str)
        self.assertIsInstance(dict_test["text"], str)

    def test_instance(self):
        """ check if amenity_1 is instance of Amenity """
        self.assertIsInstance(self.test_class, Review)
