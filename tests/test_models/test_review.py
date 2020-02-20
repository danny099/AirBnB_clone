#!/usr/bin/python3
"""Unit test Review"""
import unittest
import json
import pep8
from os import path
from models.review import Review
import models
import os


class TestBase(unittest.TestCase):
    """ Test all of i think """

    def setUp(self):
        """ Set a variable """
        self.test_class = Review

    def TestModels(self):
        """Test model name"""
        self.assertIsNotNone(
            models.review.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Review.__doc__, "No docstring in the class")

    def TestPermission(self):
        r = os.access('models/review.py', os.R_OK)
        self.assertTrue(r, "Read permissions")
        w = os.access('models/review.py', os.W_OK)
        self.assertTrue(w, "Write permissions")
        e = os.access('models/review.py', os.X_OK)
        self.assertTrue(e, "Execute permissions")

    def test_type(self):
        """Test type of class"""

        self.assertEqual(
            str(type(self.file_storage)),
            "<class 'models.review.Review'>")
        self.assertIsInstance(self.file_storage, Review)


if __name__ == '__main__':
    unittest.main()
