"""ZaaS command line interface"""

import os

import click

@click.command()
@click.argument('config', default=os.path.join(os.path.expanduser('~'),'.zanryu.json'))
def cli(config):
    """ZaaS: Zanryu as a Service"""
    with open(config, "r") as my_config:
        data = my_config.read()
    print data
