import pytest
from passly.checks.duplicates import DuplicatesCheck


@pytest.fixture
def sample_entries():
    return [
        {
            "login_uri": "https://example.com",
            "login_username": "user1",
            "login_password": "pass1",
        },
        {
            "login_uri": "https://example.com",
            "login_username": "user1",
            "login_password": "pass2",
        },
        {
            "login_uri": "https://example.com",
            "login_username": "user2",
            "login_password": "pass3",
        },
        {
            "login_uri": "https://another.com",
            "login_username": "user1",
            "login_password": "pass4",
        },
        {
            "login_uri": "https://example.com",
            "login_username": "user1 ",  # using a whitespace to test strip
            "login_password": "pass5",
        },
    ]


def test_find_duplicates(sample_entries):
    check = DuplicatesCheck(sample_entries)
    duplicates = check.find()

    # There should be 2 duplicates:
    # - The second entry is a duplicate of the first (same uri+username)
    # - The last entry also duplicates the first (after stripping)
    assert len(duplicates) == 2

    # The duplicate entries should have the expected uris and usernames
    for entry in duplicates:
        assert entry["login_uri"].strip().lower() == "https://example.com"
        assert entry["login_username"].strip().lower() == "user1"


def test_format_no_duplicates():
    check = DuplicatesCheck([])
    output = check.format([])
    assert output == "No duplicates found."


def test_format_with_duplicates(sample_entries):
    check = DuplicatesCheck(sample_entries)
    duplicates = check.find()
    output = check.format(duplicates)

    assert "Duplicate entries detected:" in output
    assert "- https://example.com (user1)" in output
