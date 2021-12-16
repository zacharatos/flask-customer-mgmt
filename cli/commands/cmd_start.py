import subprocess
import click


@click.command()
@click.argument('port', default=8000)
@click.argument('host', default='localhost')
def cli(host, port):
    """
    A click command for starting our application with gunicorn
    at host to port.
    """
    cmd = f"gunicorn -b {host}:{port} 'fcm.app:create_app()'"
    return subprocess.call(cmd, shell=True)
