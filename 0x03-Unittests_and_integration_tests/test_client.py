#!/usr/bin/env python3
"""Parameterize and patch as decorators"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url
        is the expected one based on the mocked payload"""
        return_val = {'repos_url':
                      'https://api.github.com/orgs/google/repos'}
        with patch('test_client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_public_repo:
            test_client = GithubOrgClient('google')
            mock_public_repo.return_value = return_val
            test_return = test_client._public_repos_url
            self.assertEqual(test_return,
                             mock_public_repo.return_value.get('repos_url'))

    @patch('client.get_json', return_val=[{'name': 'google'}])
    def test_public_repos(self, mock_get_json):
        """Test that the list of repos is what you expect
            from the chosen payload
           Test that the mocked property and the mocked get_json was
           called once"""
        with patch('GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value='https://api.github.com/orgs/google/repos'
                   ) as mock_repos:
            test_client = GithubOrgClient('google')
            test_return = test_client.public_repos()
            self.assertEqual(test_return, mock_get_json.get('name'))
            mock_get_json.assert_called_once
            mock_repos.assert_called_once
