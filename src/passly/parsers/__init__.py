from typing import Optional, Dict, Type, List
from passly.parsers.base import BaseParser
from passly.parsers.bitwarden import BitwardenParser

PARSERS: Dict[str, Type[BaseParser]] = {
    "bitwarden": BitwardenParser,
}


def get_parser(vendor: str, file_path: str) -> Optional[BaseParser]:
    """
    Return the appropriate parser instance based on vendor name or auto-detection.
    """
    if vendor:
        vendor = vendor.lower()
        if vendor in PARSERS:
            return PARSERS[vendor]()
        raise ValueError(f"Unsupported vendor: {vendor}")

    with open(file_path, "r", encoding="utf-8") as file:
        vendor = auto_detect_vendor(file.readline().split(","))
        return PARSERS[vendor]()


def auto_detect_vendor(header: List[str]) -> str:
    """
    Automatically detect the vendor of the input file.
    """
    for parser_cls in PARSERS.values():
        if parser_cls.detect(header):
            return parser_cls.name

    raise ValueError("Could not determine the vendor of the input file.")
