#!/usr/bin/env python3
""""Parameterize a unit test"""
import utils
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
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
    def test_get_json(self, url, resp):
        """Mock HTTP calls"""
        with patch('utils.requests') as mock_req:
            mock_resp = Mock()
            mock_req.get.return_value = mock_resp
            mock_resp.json.return_value = resp
            self.assertEqual(get_json(url), resp.json.return_value)
