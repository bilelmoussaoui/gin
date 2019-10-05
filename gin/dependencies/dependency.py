from __future__ import annotations
from abc import ABCMeta
from gin.errors import UnsupportedDependency, DependenciesNotSupported


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
    _dependencies: [Dependency]
    name: str
    is_main: bool

    @staticmethod
    def new_with_type(dependency_tag, _type: DependencyType) -> Dependency:

        if _type == DependencyType.MESON:
            from .meson import MesonDependency
            dependency = MesonDependency(dependency_tag)
        elif _type == DependencyType.CMAKE:
            from .cmake import CMakeDependency
            dependency = CMakeDependency(dependency_tag)
        elif _type == DependencyType.AUTOTOOLS:
            from .autotools import AutoToolsDependency
            dependency = AutoToolsDependency(dependency_tag)
        elif _type == Dependency.SYSTEM:
            from .system import SystemDependency
            dependency = SystemDependency(dependency_tag)
        else:
            raise UnsupportedDependency(f"{dependency_tag} is not supported")
        dependency.is_main = False  # Not a main dependency by default
        return dependency

    def __init__(self, dependency_tag):
        self.name = dependency_tag.get("name")

    def get_dependencies(self):
        if not self.is_main:
            raise DependenciesNotSupported(
                "Non-main module doesn't support sub-dependencies")

        return self._dependencies

    def get_type(self) -> DependencyType:
        return self._type
