from gin.dependencies import Dependency, DependencyType
from gin.errors import ParseError

from xml.etree import ElementTree
import pytest


def test_meson_passes():
    tag = ElementTree.fromstring(
        '''
        <meson name="something">
            <git url="https://github.com" />
            <flag name="docs">false</flag>
        </meson>
        '''
    )
    dependency = Dependency.new_with_type(tag, DependencyType.MESON)
    source = dependency.get_sources()[0]

    assert dependency.name == 'something'
    assert source.url == 'https://github.com'
    assert dependency.get_flags() == '-Ddocs=false'


def test_meson_fails():
    with pytest.raises(ParseError):
        tag = ElementTree.fromstring('<meson  />')
        Dependency.new_with_type(tag, DependencyType.MESON)
