import os
import subprocess
import click


@click.command()
@click.argument('path', default=os.path.join('fcm', 'tests'))
def cli(path):
    """
    A click command for running tests for the project.
    """
    cmd = f"py.test {path}"
    return subprocess.call(cmd, shell=True)
