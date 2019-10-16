import sys

import click

from website_worth import __version__
from website_worth.calcs import get_scraper
from website_worth.constants import (
    SUPPORTED_CALCS,
    WEBUKA
)


@click.command(help="Run website_worth.")
@click.option("-c", "--calc", required=True, type=click.Choice(SUPPORTED_CALCS), default=WEBUKA)
@click.argument("site_url", required=True, type=click.STRING)
def run(calc, site_url, **cli_kwargs):
    scraper = get_scraper(calc)
    scraper.run(site_url)


@click.command(help="Show website_worth version")
def version():
    click.echo(__version__)

# todo add invoking run subcommand when no subcommand passed
@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx, *args, **kwargs):
    pass

main.add_command(run)
main.add_command(version)

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
