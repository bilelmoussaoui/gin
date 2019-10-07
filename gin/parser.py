#
# Copyright (c) 2019 Bilal Elmoussaoui.
#
# This file is part of Gin
# (see https://github.com/bilelmoussaoui/gin).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""
    Utilities to help parsing Gin's manifest
"""
from pathlib import Path
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import ParseError as ElementTreeParseError

from gin.errors import ParseError
from gin.project import Project
from gin.dependencies import find_dependencies


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
        module = find_dependencies(self._tree)
        if len(module) != 1:
            raise ParseError("The manifest can contain only one main module")
        module = module[0]
        # Means that this module can have sub-dependencies
        module.is_main = True

        project = Project(
            id=_id,
            name=name, version=version,
            manufacturer=manufacturer,
            module=module
        )

        return project
