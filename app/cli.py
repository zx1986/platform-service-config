import click
from app.commands import vault, namespace, notify

@click.group()
def cli():
    """A multi-command CLI application."""
    pass

cli.add_command(vault.create)
cli.add_command(namespace.init)
cli.add_command(notify.send_mail)

if __name__ == "__main__":
    cli()
