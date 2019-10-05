from pathlib import Path

from gin.parser import Parser
from gin.dependencies import DependencyType


path = Path('./tests/com.belmoussaoui.GinTest.gin.xml')
parser = Parser(path)
project = parser.get_project()


def test_parse_project():

    assert project.get_id() == "com.belmoussaoui.GinTest"
    assert project.name == "GinTest"
    assert project.manufacturer == "GNOME"
    assert project.version == "3.6"


def test_parse_main_module():
    # Validate the main module
    main_module = project.module
    assert main_module.name == "gin-test"
    assert main_module.get_type() == DependencyType.MESON
    assert main_module.is_main is True


def test_parse_dependencies():
    dependencies = project.module.get_dependencies()
    assert len(dependencies) == 5
    expected_dependencies = [
        {
            "name": "gtk3",
            "type": DependencyType.SYSTEM
        },
        {
            "name": "gcc",
            "type": DependencyType.SYSTEM
        },
        {
            "name": "something",
            "type": DependencyType.MESON
        },
        {
            "name": "patched-something",
            "type": DependencyType.CMAKE
        }, {
            "name": "otherthing",
            "type": DependencyType.AUTOTOOLS
        }
    ]

    for i in range(len(dependencies)):
        dependency_test(
            dependencies[i],
            expected_dependencies[i]
        )


def dependency_test(dependency, expected):
    assert dependency.name == expected["name"]
    assert dependency.get_type() == expected['type']
