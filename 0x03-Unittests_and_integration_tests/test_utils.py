#!/usr/bin/env python3
"""A module for testing the utils module.
"""
import unittest
from parameterized import parameterized

from utils import (
    access_nested_map,
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests access_nested_map's output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
