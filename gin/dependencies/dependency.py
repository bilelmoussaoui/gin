
import os
from abc import ABCMeta, abstractmethod
from xml.etree.ElementTree import ElementTree

from logzero import logger

from gin.errors import ParseError, UnsupportedDependency
from gin.container import Container
from gin.sources import Source
from gin.template import template_env

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
    _is_main: bool
    _flags: {str: str}

    _workdir: str

    name: str
    build_only: bool

    @staticmethod
    def new_with_type(dependency_tag, _type: DependencyType):
        dependency = DependencyType.load(dependency_tag, _type)
        dependency.is_main = False
        return dependency

    @abstractmethod
    def get_flags(self):
        pass

    def __init__(self, dependency_tag: ElementTree):
        self._tree = dependency_tag
        self.name = dependency_tag.get("name")
        self.build_only = dependency_tag.get("build-only") == "true"
        self._dependencies = []
        self._flags = {}
        self._fetch_sources()
        self._fetch_flags()

    @property
    def is_main(self) -> bool:
        return self._is_main

    @is_main.setter
    def is_main(self, new_val):
        self._is_main = new_val
        if self._is_main:
            self._fetch_subdependencies()

    def prepare(self, container: Container):
        logger.info(f"Preparing {self.name}")
        self._generate_spec(container)
        spec_file = f"/data/{self.name}/{self.name}.spec"
        # Install required dependencies
        container.exec(f"dnf builddep -y {spec_file}")
        # Build rpm file
        container.exec(f"rpmbuild -bb {spec_file} --build-in-place --quiet")

    def build(self):
        pass

    def set_workdir(self, workdir):
        self._workdir = os.path.join(workdir, self.name)
        if self.get_type() != DependencyType.SYSTEM:
            # Don't create a workdir for system dependencies
            os.makedirs(self._workdir, exist_ok=True)

        for dependency in self.get_dependencies():
            dependency.set_workdir(workdir)

    def get_dependencies(self):
        return self._dependencies

    def get_main_source(self):
        if self.is_main:  # Main module source
            return self._sources[0]

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

    def _fetch_flags(self):
        flags = self._tree.findall('flag')
        for flag in flags:
            self._flags[flag.get('name')] = flag.text

    def _generate_pkgbuild(self, output_dir):
        pkg_template = template_env.get_template("PKGBUILD.in")
        pkgbuild_content = pkg_template.render(dependency=self)

        with open(os.path.join(self._workdir, "PKGBUILD"), 'w') as pkg_obj:
            pkg_obj.write(pkgbuild_content)

        if self.is_main:
            for dependency in self.get_dependencies():
                if dependency.get_type() != DependencyType.SYSTEM:
                    dependency.generate_pkgbuild()

    def _generate_spec(self, container: Container):
        pkg_template = template_env.get_template("mingw.spec.in")
        spec_content = pkg_template.render(
            dependency=self, mingw_packages=container.get_mingw_packages())
        spec_output = os.path.join(self._workdir, f"{self.name}.spec")

        with open(spec_output, 'w') as pkg_obj:
            pkg_obj.write(spec_content)
            logger.info(
                f"Spec file for {self.name} generated at {spec_output}")

        if self.is_main:
            for dependency in self.get_dependencies():
                if dependency.get_type() != DependencyType.SYSTEM:
                    dependency.generate_spec()
