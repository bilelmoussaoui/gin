from abc import ABCMeta


class DependencyType:
    SYSTEM = "system"
    MESON = "meson"
    CMAKE = "cmake"
    AUTOTOOLS = "autotools"


class Dependency(metaclass=ABCMeta):
    """ Dependency
    """
    _type: DependencyType
