from abc import ABCMeta, abstractmethod
from ..source import Source

class DependencyType:
    GIT = "git"
    ARCHIVE = "archive"
    SYSTEM = "system"


class Dependency(metaclass=ABCMeta):
    """ Dependency   
    """
    _type: DependencyType
    sources: list[Source]