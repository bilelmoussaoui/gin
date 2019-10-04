from pathlib import Path

from gin.parser import Parser


def test_parser():
    path = Path('./tests/com.belmoussaoui.GinTest.gin.xml')
    parser = Parser(path)
    project = parser.get_project()

    assert project.get_id() == "com.belmoussaoui.GinTest"
    assert project.name == "GinTest"
    assert project.manufacturer == "GNOME"
    assert project.version == "3.6"
