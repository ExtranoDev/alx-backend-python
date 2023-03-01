#!/usr/bin/env python3
""""Parameterize a unit test"""
import utils
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Parameterize a unit test
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, val1, val2, ans):
        """test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(val1, val2), ans)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, val1, val2):
        """context manager to test that a KeyError is raised for the inputs"""
        with self.assertRaises(KeyError):
            access_nested_map(val1, val2)


class TestGetJson(unittest.TestCase):
    """"Mock HTTP calls"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, url, resp, mock_get_json):
        """Mock test that utils.get_json returns expected result"""
        mock_get_json.return_value = resp
        self.assertEqual(get_json(url), resp)


class TestMemoize(unittest.TestCase):
    """ TEST Memoization """
    def test_memoize(self):
        """Test that when calling a_property twice,
            the correct result is returned but
            a_method is only called once using assert_called_once"""
        class TestClass:
            """ class """
            def a_method(self, mock_memoize):
                """ method """
                return 42

            @memoize
            def a_property(self):
                """Memoized property"""
                return self.a_method
        with patch.object(TestClass, "a_method") as mock_a_method:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock_a_method.assert_called_once
