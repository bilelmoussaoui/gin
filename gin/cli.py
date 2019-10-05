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
