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
from urllib.parse import urlparse

from gin.errors import MissingAttributeError

from .source import Source, SourceType


class ArchiveSource(Source):
    _type = SourceType.ARCHIVE

    url: str    # required: where the archive is
    sha256: str  # a hash to validate the archive
    archive_name: str  # The filename of the archive

    version: str  # The version, required by PKGBUILD.

    def __init__(self, tag):
        Source.__init__(self, tag)
        self.version = tag.get("version")
        self.url = tag.get("url")
        if not self.url:
            raise MissingAttributeError(
                "Archive source requires a url attribute")
        self.sha256 = tag.get("sha-256")
        if not self.sha256:
            raise MissingAttributeError(
                "Archive source requires a sha256 attribute")
        # Retrieve archive name
        # url -> url path -> filename -> remove extension -> remove .tar extension
        self.archive_name = os.path.splitext(
            os.path.basename(urlparse(self.url).path))[0].rstrip(".tar")

    def __str__(self):
        return self.url
