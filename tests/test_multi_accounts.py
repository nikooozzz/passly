from passly.checks import multi_accounts


def test_multiple_accounts_same_domain():
    entries = [
        {"login_uri": "https://sub1.example.com", "login_username": "user1"},
        {"login_uri": "https://sub2.example.com", "login_username": "user2"},
        {"login_uri": "https://other.com", "login_username": "user3"},
    ]
    result = multi_accounts.find_multi_accounts(entries)
    assert "example.com" in result
    assert len(result["example.com"]) == 2
