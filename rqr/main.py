import click

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo('Hello rqr!')

@cli.command()
@click.option('--save', is_flag=True, default=False)
def install(save):
    click.echo('install with{0} save'.format('' if save else 'out'))
