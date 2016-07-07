import click

from .requirements import Requirements

rqr = Requirements()

@click.group()
def cli():
    pass

@cli.command()
def list():
    try:
        requirements = rqr.pkgs
    except FileNotFoundError:
        raise click.UsageError('Requirements file not found. Call migrate or init to get started.')
    else:
        for target in requirements:
            click.echo('{}:'.format(target))
            for requirement in requirements[target]:
                version = requirements[target][requirement]
                click.echo('  - {}@{}'.format(requirement, version))

@cli.command()
@click.argument('pkg')
@click.option('--save', 'target', flag_value='base')
@click.option('--save-development', 'target', flag_value='development')
@click.option('--save-production', 'target', flag_value='production')
def install(pkg, target = None):
    rqr.install(pkg)
    if target:
        click.echo('install and save to ' + target)
    else:
        click.echo('install')
