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


class Source(metaclass=ABCMeta):
    """ Source
    """
    _type: SourceType
    _tree: ElementTree

    @staticmethod
    def new_with_type(source_tag, _type: SourceType):
        if _type == SourceType.ARCHIVE:
            from .archive import ArchiveSource
            source = ArchiveSource(source_tag)
        elif _type == SourceType.DIR:
            from .dir import DirSource
            source = DirSource(source_tag)
        elif _type == SourceType.FILE:
            from .file import FileSource
            source = FileSource(source_tag)
        elif _type == SourceType.GIT:
            from .git import GitSource
            source = GitSource(source_tag)
        elif _type == SourceType.PATCH:
            from .patch import PatchSource
            source = PatchSource(source_tag)
        else:
            raise UnsupportedSource(f"Source {source_tag} is not supported")
        return source

    def __init__(self, source_tag: ElementTree):
        self._tree = source_tag
