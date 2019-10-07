#!/usr/bin/env python
#
# Copyright (c) 2019 Bilal Elmoussaoui.
#
# This file is part of Gin
# (see https://github.com/bilelmoussaoui/gin).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from pathlib import Path
import tempfile
import os

from gin.errors import ManifestNotFound, ParseError
from gin.parser import Parser
from gin.project import Project
from gin.container import Container


class Gin:
    _manifest: Path
    _project: Project
    _container: Container  # Running container ID

    def __init__(self):
        self._workdir = tempfile.TemporaryDirectory(prefix="gin").name
        # This will run generate_pkgbuild on dependencies too

    def prepare(self):
        self._project.module.prepare(self._container)
        self._container.stop()

    def build(self):
        pass

    def set_manifest(self, manifest):
        self._manifest = Path(manifest)
        if not self._manifest.exists():
            raise ManifestNotFound(f"Manifest {manifest} not found")
        self._workdir = os.path.join(self._manifest.parent, ".gin")
        self._container = Container(self._workdir)
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
