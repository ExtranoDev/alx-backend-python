#!/usr/bin/env python3
"""Parameterize and patch as decorators"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test GitHubOrgClient"""
    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json', return_value={'payload': True})
    def test_org(self, org, mock_get):
        """test that GithubOrgClient.org returns the correct value
        make sure get_json is called once with the expected argument"""
        test_client = GithubOrgClient(org)
        test_org = test_client.org
        self.assertEqual(test_org, mock_get.return_value)
        mock_get.assert_called_once
