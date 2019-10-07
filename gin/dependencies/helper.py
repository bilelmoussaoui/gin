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


def find_dependencies(tree):
    from .dependency import Dependency, DependencyType

    supported_dependencies = DependencyType.all()
    dependencies = []

    for child in tree:
        if child.tag in supported_dependencies:
            dependencies.append(
                Dependency.new_with_type(child, child.tag)
            )
    return dependencies


def find_sources(tree):
    from gin.sources import Source, SourceType

    supported_sources = SourceType.all()
    sources = []

    for child in tree:
        if child.tag in supported_sources:
            sources.append(
                Source.new_with_type(child, child.tag)
            )
    return sources
