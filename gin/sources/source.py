from abc import ABCMeta


class SourceType:
    ARCHIVE = "archive"
    DIR = "dir"
    FILE = "file"
    PATCH = "patch"
    GIT = "git"


class Source(metaclass=ABCMeta):
    """ Source
    """
    pass
    _type: SourceType
