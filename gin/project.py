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
import os
from gin.dependencies import Dependency


class Project:

    _id: str
    name: str
    manufacturer: str
    version: str
    module: Dependency

    _workdir: str

    def __init__(self, **kwargs):
        self._id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.manufacturer = kwargs.get("manufacturer")
        self.version = kwargs.get("version")
        self.module = kwargs.get("module")

    def get_id(self):
        return self._id

    def display(self):
        print("Welcome to Gin")
        print(f"Project Name: {self.name}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Version: {self.version}")

    def bundle(self, bundle, wix_toolset_path):
        if not wix_toolset_path:
            # Fallback to our pre-shipped Wix
            wix_toolset_path = os.path.expanduser("~/wix/")

    def set_workdir(self, workdir):
        self._workdir = workdir
        self.module.set_workdir(self._workdir)
