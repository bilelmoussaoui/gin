#!/usr/bin/env python
from pathlib import Path

from gin.errors import ManifestNotFound, ParseError
from gin.parser import Parser
from gin.project import Project


class Gin:
    _manifest: Path
    _project: Project

    def __init__(self):
        pass

    def _parse(self):
        try:
            parser = Parser(self._manifest)
            self._project = parser.get_project()
        except ParseError as e:
            print(f"Failed to parse the manifest {e}")

    def manifest(self, manifest):
        path = Path(manifest)
        if not path.exists():
            raise ManifestNotFound(f"Manifest {manifest} not found")
        self._manifest = Path(manifest)
        self._parse()
        self._project.display()
        self._project.module.display()
