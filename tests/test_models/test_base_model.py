#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

class TestConsoleFunctionality(unittest.TestCase):

    def setUp(self):
        self.console = Console()

    def test_create_object_with_string_params(self):
        # Test creating an object with string parameters
        self.console.do_create("ClassA", name="\"My_house\"", location="\"New_York\"")
        # Assert that the object of ClassA was created with correct parameters
        self.assertTrue(isinstance(self.console.get_object("ClassA"), ClassA))
        self.assertEqual(self.console.get_object("ClassA").name, "My house")
        self.assertEqual(self.console.get_object("ClassA").location, "New York")

    def test_create_object_with_float_params(self):
        # Test creating an object with float parameters
        self.console.do_create("ClassB", price="10.50", rating="8.7")
        # Assert that the object of ClassB was created with correct parameters
        self.assertTrue(isinstance(self.console.get_object("ClassB"), ClassB))
        self.assertEqual(self.console.get_object("ClassB").price, 10.50)
        self.assertEqual(self.console.get_object("ClassB").rating, 8.7)

    def test_create_object_with_integer_params(self):
        # Test creating an object with integer parameters
        self.console.do_create("ClassC", quantity="5", year="2022")
        # Assert that the object of ClassC was created with correct parameters
        self.assertTrue(isinstance(self.console.get_object("ClassC"), ClassC))
        self.assertEqual(self.console.get_object("ClassC").quantity, 5)
        self.assertEqual(self.console.get_object("ClassC").year, 2022)

    def test_create_object_with_invalid_params(self):
        # Test creating an object with invalid parameters
        self.console.do_create("ClassD", invalid_param="invalid_value")
        # Assert that the object of ClassD was not created
        self.assertIsNone(self.console.get_object("ClassD"))
