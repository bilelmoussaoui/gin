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
import click

from gin.app import Gin

click_path = click.Path(exists=True, readable=True, resolve_path=True)


@click.command()
@click.argument("manifest", required=True, envvar="MANIFEST", type=click_path)
@click.argument("bundle", required=False, default="app.msi", envvar="BUNDLE")
@click.argument("wix_toolset", required=False, default="~/wix", envvar="WIX_TOOLSET")
def run(manifest, bundle, wix_toolset):
    app = Gin()
    app.set_manifest(manifest)
    app.prepare()
    app.build(bundle, wix_toolset)
