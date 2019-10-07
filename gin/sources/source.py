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
from abc import ABCMeta
from xml.etree.ElementTree import ElementTree
from gin.errors import UnsupportedSource


class SourceType:
    ARCHIVE = "archive"
    DIR = "dir"
    FILE = "file"
    PATCH = "patch"
    GIT = "git"

    @staticmethod
    def all():
        return [
            SourceType.ARCHIVE,
            SourceType.DIR,
            SourceType.FILE,
            SourceType.PATCH,
            SourceType.GIT
        ]

    @staticmethod
    def load(tag, _type):
        from .archive import ArchiveSource
        from .dir import DirSource
        from .file import FileSource
        from .git import GitSource
        from .patch import PatchSource
        types = {
            SourceType.ARCHIVE: ArchiveSource,
            SourceType.FILE: FileSource,
            SourceType.DIR: DirSource,
            SourceType.GIT: GitSource,
            SourceType.PATCH: PatchSource,
        }
        if _type not in types.keys():
            raise UnsupportedSource(f"Source of type {_type} is not supported")
        obj = types.get(_type)
        return obj(tag)


class Source(metaclass=ABCMeta):
    """ Source
    """
    _type: SourceType
    _tree: ElementTree

    @staticmethod
    def new_with_type(source_tag, _type: SourceType):
        source = SourceType.load(source_tag, _type)
        return source

    def __init__(self, source_tag: ElementTree):
        self._tree = source_tag

    def display(self):
        print(f"Source type: {self._type}")

    def get_type(self):
        return self._type
