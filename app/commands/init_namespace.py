import click


### Namespace

@click.command()
@click.argument('name')
def init_namespace(name):
    """Init namespace for new instance."""
    click.echo(f"init: {name}")
