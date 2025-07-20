from typing import Optional, Dict, Type
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

    return auto_detect_vendor(file_path)


def auto_detect_vendor(file_path: str) -> str:
    """
    Automatically detect the vendor of the input file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        header = file.readline()

    for parser_cls in PARSERS.values():
        if parser_cls.detect(header.split(",")):
            return parser_cls.name

    raise ValueError("Could not determine the vendor of the input file.")
