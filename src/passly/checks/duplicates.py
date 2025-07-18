from typing import List, Dict, Any
from passly.checks.base import Check


class DuplicatesCheck(Check):
    name = "duplicates"

    def find(self) -> List[Dict[str, Any]]:
        seen = set()
        duplicates = []
        for entry in self.entries:
            uri = entry.get("login_uri", "").strip().lower()
            username = entry.get("login_username", "").strip().lower()
            key = (uri, username)
            if key in seen:
                duplicates.append(entry)
            else:
                seen.add(key)
        return duplicates

    def format(self, results: List[Dict[str, Any]]) -> str:
        if not results:
            return "No duplicates found."
        lines = ["Duplicate entries detected:"]
        for r in results:
            lines.append(f"- {r.get('login_uri')} ({r.get('login_username')})")
        return "\n".join(lines)
