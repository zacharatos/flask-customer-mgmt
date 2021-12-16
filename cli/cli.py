import os
import click

# All our commands are inside commands folder
cmd_folder = os.path.join(os.path.dirname(__file__), 'commands')
# All our commands files starting with cmd_
cmd_prefix = 'cmd_'


class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        """
        A list with all available commands
        """
        rv = []

        # Search through all the files in the folder and
        # put in the list all the command related files
        for cmd in os.listdir(cmd_folder):
            if cmd.endswith('.py') and cmd.startswith(cmd_prefix):
                rv.append(cmd[len(cmd_prefix):-3])

        # Sort the list alphabetically
        rv.sort()

        return rv

    def get_command(self, ctx, name):
        """
        Get a specific command related to the project.
        """
        ns = {}
        fn = os.path.join(cmd_folder, cmd_prefix + name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']


@click.command(cls=CLI)
def cli():
    pass
