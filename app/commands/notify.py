import click


### Notify User

@click.command()
@click.argument('name')
def send_mail(name):
    """Greet a person by name."""
    click.echo(f"Hello, {name}!")
