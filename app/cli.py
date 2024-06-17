import click
from app.commands import create_vault, init_namespace, send_notify

@click.group()
def cli():
    """A multi-command CLI application."""
    pass

cli.add_command(create_vault.create_vault)
cli.add_command(init_namespace.init_namespace)
cli.add_command(send_notify.send_notify)

if __name__ == "__main__":
    cli()
