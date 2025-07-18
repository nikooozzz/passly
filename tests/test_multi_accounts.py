import pytest
from passly.checks.multi_accounts import MultiAccountsCheck


@pytest.fixture
def sample_entries():
    return [
        {"login_uri": "https://example.com/login", "login_username": "user1"},
        {"login_uri": "https://example.com/profile", "login_username": "user2"},
        {"login_uri": "https://sub.example.com", "login_username": "user3"},
        {"login_uri": "https://another.com", "login_username": "user4"},
        {"login_uri": "https://another.com/login", "login_username": "user5"},
        {"login_uri": "https://yetanother.org", "login_username": "user6"},
        {"login_uri": "https://yetanother.org", "login_username": "user7"},
        {"login_uri": "https://single.com", "login_username": "user8"},
    ]


def test_find_multi_accounts(sample_entries):
    check = MultiAccountsCheck(sample_entries)
    results = check.find()

    # We expect domains with more than 1 account
    assert "example.com" in results
    assert "another.com" in results
    assert "yetanother.org" in results
    assert "single.com" not in results

    assert len(results["example.com"]) == 3
    assert len(results["another.com"]) == 2
    assert len(results["yetanother.org"]) == 2


def test_format_no_multi_accounts():
    check = MultiAccountsCheck([])
    output = check.format({})
    assert output == "No multiple accounts per domain."


def test_format_with_multi_accounts(sample_entries):
    check = MultiAccountsCheck(sample_entries)
    results = check.find()
    output = check.format(results)

    assert "Domains with multiple accounts:" in output
    assert "\nexample.com:" in output
    assert "  - https://example.com/login (user1)" in output
    assert "  - https://another.com/login (user5)" in output
