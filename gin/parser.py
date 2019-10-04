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
            assert self._tree.tag == 'gin'
            assert 'id' in self._tree.attrib.keys()
        except (ElementTreeParseError, AssertionError):
            raise ParseError("Failed to parse the manifest")

    def get_project(self) -> Project:
        _id = self._tree.get('id')
        name = self._tree.find('name').text
        version = self._tree.find('version').text
        manufacturer = self._tree.find('manufacturer').text

        project = Project(
            id=_id,
            name=name, version=version,
            manufacturer=manufacturer
        )

        return project
