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

from gin.dependencies import DependencyType
from gin.parser import Parser

path = Path('./tests/org.gnome.design.Palette.gin.xml')
parser = Parser(path)
project = parser.get_project()


def test_parse_project():

    assert project.get_id() == "org.gnome.design.Palette"
    assert project.name == "Palette"
    assert project.manufacturer == "GNOME"
    assert project.version == "0.1"


def test_parse_main_module():
    # Validate the main module
    main_module = project.module
    assert main_module.name == "palette"
    assert main_module.get_type() == DependencyType.MESON
    assert main_module.is_main is True

    assert main_module.get_sources()


def test_parse_dependencies():
    dependencies = project.module.get_dependencies()
    assert len(dependencies) == 5
    expected_dependencies = [
        {
            "name": "gtk3",
            "type": DependencyType.SYSTEM
        },
        {
            "name": "gettext",
            "type": DependencyType.SYSTEM
        },
        {
            "name": "vala",
            "type": DependencyType.SYSTEM,
            "build_only": True
        },
        {
            "name": "gcc",
            "type": DependencyType.SYSTEM,
            "build_only": True
        },
        {
            "name": "meson",
            "type": DependencyType.SYSTEM,
            "build_only": True
        },
    ]

    for i in range(len(dependencies)):
        dependency_test(
            dependencies[i],
            expected_dependencies[i]
        )


def dependency_test(dependency, expected):
    assert dependency.name == expected["name"]
    assert dependency.get_type() == expected['type']
    assert dependency.build_only == expected.get("build_only", False)
