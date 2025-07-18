from passly.checks import duplicates


def test_find_duplicates_simple():
    entries = [
        {"login_uri": "https://example.com", "login_username": "user1"},
        {"login_uri": "https://example.com", "login_username": "user1"},
        {"login_uri": "https://example.com", "login_username": "user2"},
    ]
    result = duplicates.find_duplicates(entries)
    assert len(result) == 1
    assert result[0]["login_username"] == "user1"
