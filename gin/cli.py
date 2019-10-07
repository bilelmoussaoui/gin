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


@click.group()
@click.pass_context
def run(ctx):
    app = Gin()
    ctx.obj = {
        'app': app
    }


@run.command(help="Init the project by generating needed files to build")
@click.argument("manifest", required=True, envvar="MANIFEST", type=click_path)
@click.pass_context
def init(ctx, manifest):
    app = ctx.obj['app']
    app.set_manifest(manifest)
    app.prepare()


@run.command(help="Build the project")
@click.argument("bundle", required=False, envvar="BUNDLE")
@click.argument("wixtoolset", required=False, envvar="WIXTOOLSET")
@click.argument("manifest", required=True, envvar="MANIFEST", type=click_path)
@click.pass_context
def build(ctx, manifest, bundle="app.msi", wixtoolset=None):
    app = ctx.obj['app']
    app.build()
