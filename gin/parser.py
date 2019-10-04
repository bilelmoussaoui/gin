"""
    Utilities to help parsing Gin's manifest
"""
from pathlib import Path
from xml.etree.ElementTree import ElementTree

from gin.errors import ParseError


class Parser:
    _path: Path
    _tree: ElementTree

    def __init__(self, path: Path):
        self._path = path
        try:
            elem = ElementTree()
            self._tree = elem.parse(self._path)
        except Exception as e:
            print(e)
            raise ParseError("Failed to parse the manifest")
