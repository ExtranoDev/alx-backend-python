#!/usr/bin/env python3
""""""
import unittest
import utils
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
