#!/usr/bin/python3
"""Unit test FileStorage"""
import unittest
import pep8
import os
import models
from models.engine.file_storage import FileStorage


class TestFile_Storage(unittest.TestCase):
    '''start tests'''

    def test_docstring(self):
        '''test if funcions'''
        msj = "Módulo does not has docstring"
        obj = models.engine.file_storage.__doc__
        self.assertIsNotNone(obj, msj)
        msj = "Clase does not has docstring"
        self.assertIsNotNone(obj, msj)

    def test_executable_file(self):
        """test if file has permissions u+x to execute"""
        is_read_true = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """check if my_model is an instance of BaseModel"""
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)
