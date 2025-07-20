from abc import ABC, abstractmethod
from typing import List, Dict


class BaseParser(ABC):
    @abstractmethod
    def detect(self, file_path: str) -> bool:
        """Check if this parser can handle the file."""
        pass

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
