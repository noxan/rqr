import click

from .requirements import Requirements

@click.group()
def cli():
    cli.rqr = Requirements()

@cli.command()
def list():
    click.echo(cli.rqr)

@cli.command()
@click.argument('pkgs', nargs=-1)
@click.option('--save', 'target', flag_value='base')
@click.option('--save-development', 'target', flag_value='development')
@click.option('--save-production', 'target', flag_value='production')
def install(pkgs, target = None):
    click.echo(cli.rqr.install(pkgs, target))

@cli.command()
def migrate():
    cli.rqr.migrate()

@cli.command()
def update():
    updates = cli.rqr.update()
    if len(updates) is 0:
        click.echo('No updates found.')
    for update in updates:
        click.echo('{0} {1} -> {2}'.format(*update))
