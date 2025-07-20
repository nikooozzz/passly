from passly.parsers.bitwarden import BitwardenParser
from passly.parsers import auto_detect_vendor


def test_bitwarden_detect_exact():
    header = [
        "folder",
        "favorite",
        "type",
        "name",
        "notes",
        "fields",
        "reprompt",
        "login_uri",
        "login_username",
        "login_password",
        "login_totp",
    ]
    assert BitwardenParser.detect(header) is True


def test_bitwarden_detect_case_insensitive():
    header = [
        "Folder",
        " Favorite ",
        "TYPE",
        "name",
        "notes",
        "fields",
        "reprompt",
        "LOGIN_URI",
        "LOGIN_USERNAME",
        "LOGIN_PASSWORD",
        "LOGIN_TOTP",
    ]
    assert BitwardenParser.detect(header) is True


def test_bitwarden_detect_invalid():
    header = ["username", "password", "url"]
    assert BitwardenParser.detect(header) is False


def test_auto_detect_bitwarden():
    header = [
        "folder",
        "favorite",
        "type",
        "name",
        "notes",
        "fields",
        "reprompt",
        "login_uri",
        "login_username",
        "login_password",
        "login_totp",
    ]
    assert auto_detect_vendor(header) == "bitwarden"
