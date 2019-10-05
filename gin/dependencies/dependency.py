
from abc import ABCMeta
from xml.etree.ElementTree import ElementTree

from gin.sources import Source
from gin.errors import (UnsupportedDependency, DependenciesNotSupported,
                        ParseError)
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

    @staticmethod
    def load(tag, _type):
        from .meson import MesonDependency
        from .cmake import CMakeDependency
        from .autotools import AutotoolsDependency
        from .system import SystemDependency
        types = {
            DependencyType.MESON: MesonDependency,
            DependencyType.CMAKE: CMakeDependency,
            DependencyType.AUTOTOOLS: AutotoolsDependency,
            DependencyType.SYSTEM: SystemDependency,
        }
        if _type not in types.keys():
            raise UnsupportedDependency(f"{tag} is not supported")
        obj = types.get(_type)
        return obj(tag)


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
        dependency = DependencyType.load(dependency_tag, _type)
        dependency.is_main = False
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

    def get_sources(self):
        if self._type == DependencyType.SYSTEM:
            raise ParseError("System dependencies don't support sources")
        return self._sources

    def display(self):
        if self.is_main:
            print(f"Main Module: {self.name}")
            print(f"Type: {self._type}")
        else:
            print(f"\tDependency: {self.name}")
            print(f"\tType: {self._type}")

        if self._type != DependencyType.SYSTEM:
            for source in self.get_sources():
                source.display()

        if self.is_main:
            for dependency in self.get_dependencies():
                dependency.display()

    def get_type(self) -> DependencyType:
        return self._type

    def _fetch_subdependencies(self):
        tree = self._tree.find('dependencies')
        dependencies = find_dependencies(tree)
        self._dependencies = dependencies

    def _fetch_sources(self):
        sources = find_sources(self._tree)
        if not sources and self._type != DependencyType.SYSTEM:
            raise ParseError("Dependency should have at least one source")
        self._sources = sources
