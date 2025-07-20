from typing import List, Dict
from passly.parsers.base import BaseParser


class BitwardenParser(BaseParser):
    name = "bitwarden"

    EXPECTED_COLUMNS = [
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

    def parse(self, rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
        return [
            {
                "name": row.get("name", "").strip(),
                "uri": row.get("login_uri", "").strip(),
                "username": row.get("login_username", "").strip(),
                "password": row.get("login_password", "").strip(),
                "notes": row.get("notes", "").strip(),
            }
            for row in rows
        ]
