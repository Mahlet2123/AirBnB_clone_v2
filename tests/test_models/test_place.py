#!/usr/bin/python3
"""
Tests for the Place Model
"""


import unittest
import datetime

from models.place import Place

class TestPlace(unittest.TestCase):
    """Testing the place Module"""

    def setUp(self):
        """An instance just for tests"""
        self.a1 = Place()
        self.a2 = Place()

    def test_instances(self):
        """Test the instances"""
        self.assertTrue(isinstance(self.a1, Place))
        self.assertTrue(isinstance(self.a2, Place))
        self.assertTrue(hasattr(self.a1, "city_id"))
        self.assertTrue(hasattr(self.a1, "user_id"))
        self.assertTrue(hasattr(self.a1, "name"))
        self.assertTrue(hasattr(self.a1, "description"))
        self.assertTrue(hasattr(self.a1, "number_rooms"))
        self.assertTrue(hasattr(self.a1, "number_bathrooms"))
        self.assertTrue(hasattr(self.a1, "max_guest"))
        self.assertTrue(hasattr(self.a1, "price_by_night"))
        self.assertTrue(hasattr(self.a1, "latitude"))
        self.assertTrue(hasattr(self.a1, "longitude"))
        self.assertTrue(hasattr(self.a1, "amenity_ids"))

    def test_city_id(self):
        """test the city_id"""
        self.assertEqual(type(self.a1.city_id), str)
        self.assertEqual(self.a1.city_id, "")
        self.assertNotEqual(self.a1.city_id, None)

    def test_name(self):
        """test the name"""
        self.assertEqual(type(self.a1.name), str)
        self.assertEqual(self.a1.name, "")
        self.assertNotEqual(self.a1.name, None)


if __name__ == '__main__':
    unittest.main()
