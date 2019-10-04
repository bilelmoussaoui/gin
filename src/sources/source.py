from abc import ABCMeta, abstractmethod


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
