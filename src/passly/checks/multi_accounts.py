from typing import List, Dict, Any
import tldextract
from collections import defaultdict
from passly.checks.base import Check


class MultiAccountsCheck(Check):
    name = "multi_accounts"

    def find(self) -> Dict[str, List[Dict[str, Any]]]:
        grouped = defaultdict(list)
        for entry in self.entries:
            uri = entry.get("login_uri", "").strip().lower()
            if uri:
                domain_parts = tldextract.extract(uri)
                base_domain = f"{domain_parts.domain}.{domain_parts.suffix}"
                grouped[base_domain].append(entry)

        return {
            domain: entries for domain, entries in grouped.items() if len(entries) > 1
        }

    def format(self, results: Dict[str, List[Dict[str, Any]]]) -> str:
        if not results:
            return "No multiple accounts per domain."
        lines = ["Domains with multiple accounts:"]
        for domain, entries in results.items():
            lines.append(f"\n{domain}:")
            for e in entries:
                lines.append(f"  - {e.get('login_uri')} ({e.get('login_username')})")
        return "\n".join(lines)
