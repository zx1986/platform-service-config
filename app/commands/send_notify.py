import click


### Notify User

@click.command()
@click.argument('name')
def send_notify(name):
    """Send info to owner of instance."""
    click.echo(f"Hello, {name}!")
