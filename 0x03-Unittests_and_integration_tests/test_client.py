#!/usr/bin/env python3
"""A module for testing the client module.
"""
import unittest
from typing import Dict
from parameterized import parameterized
from unittest.mock import MagicMock, patch

from client import (
    GithubOrgClient
)


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """Tests the `org` method."""
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
            self,
            repo: Dict,
            license_key: str,
            has_key: bool,
            ) -> None:
        """Tests the `has_license` method."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            has_key,
        )
