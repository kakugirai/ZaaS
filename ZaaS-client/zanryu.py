"""ZaaS command line interface"""
# encoding: utf-8

import os
import json
from datetime import date

import requests
import click

URL = "http://127.0.0.1:5000/zanryu"

@click.command()
@click.argument('config', default=os.path.join(os.path.expanduser('~'), '.zanryu.json'))
def cli(config):
    """ZaaS: Zanryu as a Service"""
    with open(config, "r") as file:
        data = json.load(file)
    weekdays = ["月", "火", "水", "木", "金", "土", "日"]
    i = date.today()
    data["login_name"] = os.getlogin()
    data["year"] = i.year
    data["month"] = i.month
    data["day"] = i.day
    data["weekday"] = weekdays[i.weekday()]
    r = requests.post(URL, json=data)
    return

