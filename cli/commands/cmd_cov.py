import subprocess
import click


@click.command()
@click.argument('path', default='fcm')
def cli(path):
    """
    Run a command from click interface to test the
    code coverage.
    """
    cmd = f"py.test --cov-report term-missing --cov {path}"
    return subprocess.call(cmd, shell=True)
