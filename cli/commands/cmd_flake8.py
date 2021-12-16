import subprocess
import click


@click.command()
@click.option('--skip-init/--no-skip-init',
              default=True,
              help='Flag for skipping __init__.py files.')
@click.argument('path', default='fcm')
def cli(skip_init, path):
    """
    A click command for checking our code against PEP8
    standards so we are coding in a unified format.
    """

    # Check against click options
    flake8_exclude = ''
    if skip_init:
        flake8_exclude = '--exclude __init__.py'

    cmd = f"flake8 {path} {flake8_exclude}"
    return subprocess.call(cmd, shell=True)
