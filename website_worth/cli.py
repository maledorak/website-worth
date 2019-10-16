import sys

import click

from website_worth import __version__
from website_worth.constants import (
    SUPPORTED_CALCS
)


@click.group()
def main():
    pass


@click.command(help="Run website_worth.")
@click.option("-c", "--calc", required=True, type=click.Choice(SUPPORTED_CALCS))
def run(calc, **cli_kwargs):
    print(calc)


@click.command(help="Show website_worth version")
def version():
    click.echo(__version__)


main.add_command(run)
main.add_command(version)

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
