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
        except ElementTreeParseError:
            raise ParseError("Failed to parse the manifest")

    def get_project(self) -> Project:
        #    project_id =
        root = self._tree

        assert root.tag == 'gin'
        assert 'id' in root.attrib.keys()

        for child in root:
            if child.tag == "name":
                name = child.text
                print(name)
            elif child.tag == "version":
                version = child.text
            elif child.tag == "manufacturer":
                manufacturer = child.text

        project = Project(
            id=root.attrib['id'],
            name=name, version=version,
            manufacturer=manufacturer
        )

        return project
