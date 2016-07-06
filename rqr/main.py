import click

from .requirements import load_requirements

@click.group()
def cli():
    pass

@cli.command()
def list():
    try:
        requirements = load_requirements()
    except FileNotFoundError:
        raise click.UsageError('Requirements file not found. Call migrate or init to get started.')
    else:
        for target in requirements:
            click.echo('{}:'.format(target))
            for requirement in requirements[target]:
                version = requirements[target][requirement]
                click.echo('  - {}@{}'.format(requirement, version))

@cli.command()
@click.option('--save', 'target', flag_value='base')
@click.option('--save-development', 'target', flag_value='development')
@click.option('--save-production', 'target', flag_value='production')
def install(target = None):
    if target:
        click.echo('install and save to ' + target)
    else:
        click.echo('install')
