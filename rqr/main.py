import click

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo('Hello rqr!')

@cli.command()
@click.option('--save', 'target', flag_value='base')
@click.option('--save-development', 'target', flag_value='development')
@click.option('--save-production', 'target', flag_value='production')
def install(target = None):
    if target:
        click.echo('install and save to ' + target)
    else:
        click.echo('install')
