import click

@click.group()
def cli():
    pass

@click.command()
def hello():
    click.echo('Hello rqr!')
cli.add_command(hello)
