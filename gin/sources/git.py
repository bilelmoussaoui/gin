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
from .source import Source, SourceType
from gin.errors import MissingAttributeError


class GitSource(Source):
    _type = SourceType.GIT
    url: str 	# required: where the repo is
    commit: str  # a specific commit to use
    tag: str 	# the tag to use
    branch: str  # the branch to use

    def __init__(self, tag):
        Source.__init__(self, tag)
        self.url = tag.get("url")
        if not self.url:
            raise MissingAttributeError("Git source requires a url attribute")
        self.commit = tag.get("commit")
        self.branch = tag.get("branch")
        self.tag = tag.get("tag")

    def __str__(self):
        return f"git+{self.url}"
