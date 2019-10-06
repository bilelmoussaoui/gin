#!/usr/bin/env python
from pathlib import Path
import tempfile
import os

from gin.errors import ManifestNotFound, ParseError
from gin.parser import Parser
from gin.project import Project


class Gin:
    _manifest: Path
    _project: Project

    def __init__(self):
        self._workdir = tempfile.TemporaryDirectory(prefix="gin").name

    def prepare(self):
        # This will run generate_pkgbuild on dependencies too
        self._project.module.prepare()

    def build(self):
        pass

    def set_manifest(self, manifest):
        self._manifest = Path(manifest)
        if not self._manifest.exists():
            raise ManifestNotFound(f"Manifest {manifest} not found")
        self._workdir = os.path.join(self._manifest.parent, ".gin")
        self._parse()

    def run(self):
        self._project.display()
        self._project.module.display()

    def _parse(self):
        try:
            parser = Parser(self._manifest)
            self._project = parser.get_project()
            self._project.set_workdir(self._workdir)
        except ParseError as e:
            print(f"Failed to parse the manifest {e}")
