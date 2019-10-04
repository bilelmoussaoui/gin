"""
    Utilities to help parsing Gin's manifest
"""
from pathlib import Path
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import ParseError as ElementTreeParseError

from gin.errors import ParseError
from gin.project import Project


class Parser:
    _path: Path
    _tree: ElementTree

    def __init__(self, path: Path):
        self._path = path
        try:
            elem = ElementTree()
            self._tree = elem.parse(self._path)
            print(self._tree)
        except ElementTreeParseError:
            raise ParseError("Failed to parse the manifest")

    def get_project(self) -> Project:
        pass
