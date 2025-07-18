import sys
from typing import Optional
from passly.config import RED, YELLOW, RESET


class OutputManager:
    def __init__(self, output_path: Optional[str] = None, color: bool = True):
        self.output_path = output_path
        self.color = color and self._supports_color()

    def _supports_color(self) -> bool:
        if sys.platform == "win32":
            return True
        return sys.stdout.isatty()

    def print(self, text: str):
        if self.output_path:
            self._write_file(text)
        else:
            self._print_console(text)

    def _print_console(self, text: str):
        if self.color:
            text = self._colorize(text)
        print(text)

    def _write_file(self, text: str):
        with open(self.output_path, "w", encoding="utf-8") as f:
            f.write(text)

    def _colorize(self, text: str) -> str:
        lines = []
        for line in text.splitlines():
            if line.startswith("ERROR"):
                line = f"{RED}{line}{RESET}"
            elif line.startswith("WARNING"):
                line = f"{YELLOW}{line}{RESET}"
            lines.append(line)
        return "\n".join(lines)
