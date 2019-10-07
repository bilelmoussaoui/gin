from pathlib import Path

from gin.parser import Parser
from gin.dependencies import DependencyType


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
    assert len(dependencies) == 4
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
