#!/usr/bin/env python3
"""Implement the tests for the utils module."""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import (access_nested_map, get_json, memoize)

class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that the function returns the expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that the function raises the expected exception."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError: ('{expected}')", repr(context.exception))


class TestGetJson(unittest.TestCase):
    """Test the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that the function returns the expected result."""
        config = {"return_value.json.return_value": test_payload}
        patcher = patch("requests.get", **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """Test the memoize decorator."""

    @patch("utils.TestClass.a_method")
    def test_memoize(self, mock_a_method):
        """Test that the memoize decorator caches the result of a method."""
        
        class TestClass:
            """Test class for memoization."""
            def a_method(self):
                """Return 42."""
                return 42

            @memoize
            def a_property(self):
                """Return the result of a_method."""
                return self.a_method()
            
        with patch.object(TestClass, "a_method") as mock_a_method:
            test_class = TestClass
            test_class.a_property()
            test_class.a_property()
            mock_a_method.assert_called_once()
