
from abc import ABCMeta
from xml.etree.ElementTree import ElementTree

from gin.sources import Source
from gin.errors import UnsupportedDependency, DependenciesNotSupported
from .helper import find_dependencies, find_sources


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
    _tree: ElementTree
    _type: DependencyType
    _dependencies: []
    _sources: [Source]
    name: str
    _is_main: bool

    @staticmethod
    def new_with_type(dependency_tag, _type: DependencyType):

        if _type == DependencyType.MESON:
            from .meson import MesonDependency
            dependency = MesonDependency(dependency_tag)
        elif _type == DependencyType.CMAKE:
            from .cmake import CMakeDependency
            dependency = CMakeDependency(dependency_tag)
        elif _type == DependencyType.AUTOTOOLS:
            from .autotools import AutoToolsDependency
            dependency = AutoToolsDependency(dependency_tag)
        elif _type == DependencyType.SYSTEM:
            from .system import SystemDependency
            dependency = SystemDependency(dependency_tag)
        else:
            raise UnsupportedDependency(f"{dependency_tag} is not supported")
        dependency.is_main = False  # Not a main dependency by default
        return dependency

    def __init__(self, dependency_tag: ElementTree):
        self._tree = dependency_tag
        self.name = dependency_tag.get("name")
        self._fetch_sources()

    @property
    def is_main(self) -> bool:
        return self._is_main

    @is_main.setter
    def is_main(self, new_val):
        self._is_main = new_val
        if self._is_main:
            self._fetch_subdependencies()

    def get_dependencies(self):
        if not self.is_main:
            raise DependenciesNotSupported(
                "Non-main module doesn't support sub-dependencies")

        return self._dependencies

    def get_type(self) -> DependencyType:
        return self._type

    def _fetch_subdependencies(self):
        tree = self._tree.find('dependencies')
        dependencies = find_dependencies(tree)
        self._dependencies = dependencies

    def _fetch_sources(self):
        sources = find_sources(self._tree)
        self._sources = sources
