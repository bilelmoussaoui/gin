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
from xml.etree import ElementTree

from gin.errors import ParseError

from .dependency import Dependency, DependencyType


class SystemDependency(Dependency):

    @staticmethod
    def new(dependency_name: str):
        tag = ElementTree.fromstring(f"<system name='{dependency_name}' />")
        return SystemDependency(tag)

    def __init__(self, tag):
        self._type = DependencyType.SYSTEM
        Dependency.__init__(self, tag)

    def get_flags(self):
        raise ParseError("System dependencies don't support flags")
