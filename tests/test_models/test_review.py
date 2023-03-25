#!/usr/bin/python3
"""
Tests for the Review Model
"""


import unittest
import datetime

from models.review import Review


class TestReview(unittest.TestCase):
    """Test the Reviews"""
   
    def setUp(self):
        """Instances for testing"""
        self.c1 = Review()
        self.c2 = Review()

    def test_instances(self):
        """Check the instances and presence of attributes"""
        self.assertIsInstance(self.c1, Review)
        self.assertIsInstance(self.c2, Review)
        self.assertTrue(hasattr(self.c1, "place_id"))
        self.assertTrue(hasattr(self.c1, "user_id"))
        self.assertTrue(hasattr(self.c1, "text"))

    def test_place_id(self):
        """Test the place_id attribute"""
        self.assertEqual(type(self.c1.place_id), str)
        self.assertEqual(self.c1.place_id, "")
        self.assertNotEqual(self.c1.place_id, None)

    def test_user_id(self):
        """Test the user_id attribute"""
        self.assertNotEqual(self.c1.user_id, None)
        self.assertEqual(type(self.c1.user_id), str)
        self.assertEqual(self.c1.user_id, "")

    def test_text(self):
        """Test the text attribute"""
        self.assertNotEqual(self.c1.text, None)
        self.assertEqual(type(self.c1.text), str)
        self.assertEqual(self.c1.text, "")


if __name__ == '__main__':
    unittest.main()
