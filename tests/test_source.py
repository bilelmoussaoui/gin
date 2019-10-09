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

import pytest

from gin.errors import MissingAttributeError
from gin.sources import Source, SourceType


def test_git_passes():
    tag = ElementTree.fromstring(
        '<git url="https://gitlab.gnome.org/world/design/palette.git" branch="master" />')
    source = Source.new_with_type(tag, SourceType.GIT)

    assert source.url == "https://gitlab.gnome.org/world/design/palette.git"
    assert source.branch == 'master'
    assert source.commit is None
    assert source.tag is None


def test_git_fails():
    with pytest.raises(MissingAttributeError):
        tag = ElementTree.fromstring('<git  />')
        Source.new_with_type(tag, SourceType.GIT)


def test_archive_passes():
    tag = ElementTree.fromstring(
        '<archive url="https://gitlab.gnome.org/World/design/contrast/contrast-0.0.2.tar.xz" sha-256="test" />')
    source = Source.new_with_type(tag, SourceType.ARCHIVE)

    assert source.url == "https://gitlab.gnome.org/World/design/contrast/contrast-0.0.2.tar.xz"
    assert source.sha256 == "test"


def test_archive_fails():
    with pytest.raises(MissingAttributeError):
        tag = ElementTree.fromstring(
            '<archive url="https://gitlab.gnome.org/World/design/contrast/contrast-0.0.2.tar.xz"  />')
        Source.new_with_type(tag, SourceType.ARCHIVE)


def test_patch_passes():
    tag = ElementTree.fromstring('<patch path="appdata.patch" />')
    source = Source.new_with_type(tag, SourceType.PATCH)

    assert source.path == "appdata.patch"


def test_patch_fails():
    with pytest.raises(MissingAttributeError):
        tag = ElementTree.fromstring('<patch  />')
        Source.new_with_type(tag, SourceType.PATCH)
