import click
import hvac


### Vault

@click.command()
@click.argument('name')
def create_vault(name):
    """Create vault for new instance."""
    click.echo(f"create vault: {name}")
