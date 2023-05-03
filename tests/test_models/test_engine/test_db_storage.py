#!/usr/bin/python3
"""
Tests for File Storage
"""
import unittest
import datetime
import pycodestyle
import models.engine.db_storage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City


class Test_DBStotage(unittest.TestCase):
    """ Class for testing the db storage module"""

    def setUp(self):
        """ sets up DBStorage by creating an instance """
        self.storage = DBStorage()
        self.storage.reload()

    def tearDown(self):
        """ Closes the session after test is completed """
        self.storage.__session.close()

    def test_dbstorage_confirm_pycode(self):
        """ test adherance to pycodestyle """
        pycode = pycodestyle.StyleGuide(quiet=True)
        result = pycode.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                "Found code style errors (and warnings).")

    def test_dbstorage_doc_string(self):
        """ test the existence of db_storage's docstring """
        self.assertIsNot(models.engine.db_storage.__doc__, None,
                "db_storage needs a docstring")
        self.assertTrue(len(models.engine.file_storage.__doc__) >= 1,
                "db_storage needs a docstring")
    def test_create_state(self):
        """Tests that a new state can be created and retrieved"""
        new_state = State(name="California")
        self.storage.new(new_state)
        self.storage.save()
        all_states = self.storage.all(State)
        self.assertIn(new_state, all_states.values())

    def test_create_city(self):
        """Tests that a new city can be created and retrieved"""
        new_state = State(name="California")
        self.storage.new(new_state)
        new_city = City(name="Fremont", state_id=new_state.id)
        self.storage.new(new_city)
        self.storage.save()
        all_cities = self.storage.all(City)
        self.assertIn(new_city, all_cities.values())

    def test_create_city_with_space_in_name(self):
        """Tests that a new city with a space in the name can be created and retrieved"""
        new_state = State(name="California")
        self.storage.new(new_state)
        new_city = City(name="San Francisco", state_id=new_state.id)
        self.storage.new(new_city)
        self.storage.save()
        all_cities = self.storage.all(City)
        self.assertIn(new_city, all_cities.values())

    def test_state_present(self):
        """Test whether a State with name 'California' is present or not"""
                state = State(name='California')
        storage.new(state)
        storage.save()
        all_states = storage.all(State)
        for st in all_states.values():
            if st.name == 'California':
                found = True
                break
        else:
            found = False
        self.assertTrue(found, "State with name 'California' not found")

if __name__ == '__main__':
    unittest.main()
