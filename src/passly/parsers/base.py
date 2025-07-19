from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseParser(ABC):
    @abstractmethod
    def detect(self, file_path: str) -> bool:
        """Check if this parser can handle the file."""
        pass

    @abstractmethod
    def parse(self, file_path: str) -> List[Dict[str, Any]]:
        """Convert the file into a normalized format"""
        pass
