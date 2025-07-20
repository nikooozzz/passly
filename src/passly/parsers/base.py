from abc import ABC, abstractmethod
from typing import List, Dict


class BaseParser(ABC):
    name: str = "base"

    @classmethod
    def detect(cls, header: List[str]) -> bool:
        """Check if this parser can handle the file."""
        return [col.strip().lower() for col in header] == cls.EXPECTED_COLUMNS

    @abstractmethod
    def parse(self, file_path: str) -> List[Dict[str, str]]:
        """
        Parse the file and return a list of entries as dictionaries.
        Each dict should have normalized keys:
        - login_uri
        - login_username
        - login_password
        - login_totp
        """
        pass
