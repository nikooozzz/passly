from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional
from passly.output import OutputManager


class Check(ABC):
    """
    Abstract base class for all checks.
    Provides structure for implementing consiistent check behavior.
    """

    name: str = "base"

    def __init__(
        self,
        entries: List[Dict[str, Any]],
        config: Optional[dict] = None,
        output: Optional[OutputManager] = None,
    ):
        self.entries = entries
        self.config = config or {}
        self.output = output or OutputManager()

    @abstractmethod
    def find(self) -> Any:
        """
        Core logic for the check.
        Must return raw results (list, dict, etc.)
        """
        pass

    def format(self, results: Any) -> str:
        """
        Convert raw results into a human-readable string.
        Override in subclasses for custom formatting.
        """
        return str(results)

    def run(self) -> Any:
        """
        Executes the check:
        - Runs `find()`to compute results
        - Formats results with `format()`
        - Sends output to OutputManager
        """
        results = self.find()
        formatted = self.format(results)

        if self.output:
            self.output.print(f"[{self.name}] Results:\n{formatted}")

        return results
