#!/usr/bin/env python3
"""Module to test client file"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
import json


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class to test GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        GithubOrgClient(org_name).org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.get_json')
    def test_public_repos_url(self, org_name, mock_get_json):
        """Test that GithubOrgClient._public_repos_url
        returns the correct value
        """
        GithubOrgClient(org_name)._public_repos_url
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the correct value"""
        payload = [{"name": "google"}, {"name": "Twitter"}]
        mock_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "hello/world"
            result = GithubOrgClient('test').public_repos()

            check = [i['name'] for i in payload]
            self.assertEqual(result, check)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license returns the correct value"""
        test = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(test, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)

class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        config = {'return_value.json.side_effect': [
            cls.org_payload, cls.repos_payload,
            cls.repos_payload,cls.repos_payload
        ]}
        cls.get_patcher = patch('requests.get', **config)
        cls.mock_get = cls.get_patcher.start()

    def test_public_repos(self):
        """Test public repos"""
        test = GithubOrgClient('google')
        self.assertEqual(test.public_repos(), self.expected_repos)
        self.assertEqual(test.public_repos("XLICENSE"), [])
        self.assertEqual(test.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock_get.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Tear down class"""
        cls.get_patcher.stop()
