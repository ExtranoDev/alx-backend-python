#!/usr/bin/env python3
"""Parameterize and patch as decorators"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from urllib.error import HTTPError
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that the list of repos is what you expect
            from the chosen payload
           Test that the mocked property and the mocked get_json was
           called once"""
        mock_get_json.return_value = [{
                                'repos_url': 'https://google/repo',
                                'name': 'google_repo'
                                }]
        with patch('GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value='https://api.github.com/orgs/google/repos'
                   ) as mock_repos:
            test_client = GithubOrgClient('google')
            test_return = test_client.public_repos()
            self.assertEqual(['google'], mock_get_json.get('name'))
            mock_get_json.assert_called_once()
            mock_repos.assert_called_once()

    @parameterized.expand([
                            ({"license": {"key": "my_license"}},
                             "my_license", True),
                            ({"license": {"key": "other_license"}},
                             "my_license", False)
                          ])
    def test_has_license(self, repo, license_key, output):
        """Test if License exists"""
        test_client = GithubOrgClient('google')
        test_output = test_client.has_license(repo, license_key)
        self.assertEqual(test_output, output)


@parameterized_class(("org_payload", "repos_payload",
                     "expected_repos", "apache2_repos"),
                     TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test """
    @classmethod
    def setUpClass(cls):
        """ mock function to return example payloads
        found in the fixtures"""
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClas(cls):
        """ Stop Patcher """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Implement the test_public_repos method to test
        GithubOrgClient.public_repos"""
        test_class = GithubOrgClient('google')
        assert True

    def test_public_repos_with_license(self):
        """Implement test_public_repos_with_license to
        test the public_repos"""
        test_class = GithubOrgClient('google')
        assert True
