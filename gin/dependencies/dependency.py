from abc import ABCMeta
from gin.errors import UnsupportedDependency


class DependencyType:
    SYSTEM = "system"
    MESON = "meson"
    CMAKE = "cmake"
    AUTOTOOLS = "autotools"

    @staticmethod
    def all():
        return [
            DependencyType.CMAKE,
            DependencyType.MESON,
            DependencyType.AUTOTOOLS,
            DependencyType.SYSTEM
        ]


class Dependency(metaclass=ABCMeta):
    """ Dependency
    """
    _type: DependencyType
    name: str

    @staticmethod
    def new_with_type(dependency, _type: DependencyType):

        if _type == DependencyType.MESON:
            from .meson import MesonDependency
            return MesonDependency(dependency)
        elif _type == DependencyType.CMAKE:
            from .cmake import CMakeDependency
            return CMakeDependency(dependency)
        elif _type == DependencyType.AUTOTOOLS:
            from .autotools import AutoToolsDependency
            return AutoToolsDependency(dependency)
        elif _type == Dependency.SYSTEM:
            from .system import SystemDependency
            return SystemDependency(dependency)
        else:
            raise UnsupportedDependency(f"{dependency} is not supported")

    def __init__(self, dependency_tag):
        self.name = dependency_tag.get("name")

    def get_type(self) -> DependencyType:
        return self._type
