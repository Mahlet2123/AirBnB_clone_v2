#!/usr/bin/python3
"""
Tests for File Storage
"""
import unittest
import datetime
import pycodestyle
import models.engine.file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFilestorage (unittest.TestCase):
    """ class for testing the file storage module """
    def setUp(self):
        """ set up filestorage by creating an instance """
        self.storage = FileStorage()

    def tearDown(self):
        """ delete instances after test is completed """
        del self.storage

    def test_filestorage_confirm_pycode(self):
        """ test adherance to pycodestyle """
        pycode = pycodestyle.StyleGuide(quiet=True)
        result = pycode.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                "Found code style errors (and warnings).")

    def test_filestorage_doc_string(self):
        """ test the existence of file_storage's docstring """
        self.assertIsNot(models.engine.file_storage.__doc__, None,
                "file_storage needs a docstring")
        self.assertTrue(len(models.engine.file_storage.__doc__) >= 1,
                "file_storage needs a docstring")

    def test_new(self):
        """ Test that new() sets the object in __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertTrue("{}.{}".format(type(obj).__name__, obj.id) in self.storage.all())

    def test_all(self):
        """ test all() returns the dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_save(self):
        """ Test that save() serializes __objects to the JSON file """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, "r") as r:
            self.assertIn(obj.id, r.read())

    def test_reload(self):
        """ test that reload() deserializes the JSON file to __objects """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        obj_key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(obj_key, self.storage.all())

if __name__ == '__main__':
    unittest.main()
