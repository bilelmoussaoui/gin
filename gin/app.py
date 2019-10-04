#!/usr/bin/env python
from pathlib import Path

from gin.errors import ManifestNotFound, ParseError
from gin.parser import Parser

class Gin:
    _manifest: Path

    def __init__(self):
        pass

    def _parse(self):
        try:
            parser = Parser(self._manifest)
        except ParseError:
            print("Failed to parse the manifest")

    def manifest(self, manifest):
        path = Path(manifest)
        if not path.exists():
            raise ManifestNotFound(f"Manifest {manifest} not found")
        self._manifest = Path(manifest)
        self._parse()

