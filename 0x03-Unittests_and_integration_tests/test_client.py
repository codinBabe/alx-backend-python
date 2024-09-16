#!/usr/bin/env python3
"""Module to test client file"""

import unittest
from unittest.mock import patch , PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


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
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    

    @patch('client.get_json')
    def test_public_repos_url(self, org_name, mock_get_json):
        """Test that GithubOrgClient._public_repos_url returns the correct value"""
        GithubOrgClient(org_name)._public_repos_url
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")



    @patch('client.get_json')
    def test_public_repos(self, org_name, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the correct value"""
        GithubOrgClient(org_name).public_repos()
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        mock_get_json.reset_mock()
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = f"https://api.github.com/orgs/{org_name}/repos"
            GithubOrgClient(org_name).public_repos()
            mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}/repos")
