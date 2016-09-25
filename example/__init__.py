"""
An example CLI made using HelCLI
"""
from helcli import HelCLI


def main():
    # sub_module where our sub_commands are located
    sub_commands = 'commands'
    # description of our CLI
    description = 'An example CLI'
    # config file location, in this example these are invalid
    config_loc = ['/etc/example.conf', '.example.conf']
    cli = HelCLI(sub_commands, description, config_loc)
    cli.run()

# vim:et:fdm=marker:sts=4:sw=4:ts=4
