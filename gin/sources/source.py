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
