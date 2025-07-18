# =========================================
# Utility functions for Bitwarden Checker
# =========================================

import tldextract


def get_registered_domain(url: str) -> str:
    """
    Extract the registered domain from a given URL.
    For example:
      'https://sub.example.co.uk/path' -> 'example.co.uk'
    """
    if not url:
        return ""
    ext = tldextract.extract(url)
    return f"{ext.domain}.{ext.suffix}" if ext.suffix else ext.domain


def normalize_whitespace(text: str) -> str:
    """
    Remove extra spaces and normalize input text.
    """
    return text.strip() if text else ""


def is_valid_bitwarden_row(row: dict, required_fields: list) -> bool:
    """
    Validate that a CSV row contains the required fields.
    """
    return all(field in row for field in required_fields)
