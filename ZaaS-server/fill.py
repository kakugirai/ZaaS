# -*- coding: utf-8 -*-

import os
import json
from bs4 import BeautifulSoup


def fill_html(json_dir, blank_html="blank.html", unit_html="unit.html"):
    """
    The function will read all json files in json_dir and save formatted
    HTML file to a zanryu.html
    @type json_data: str
    @param json_data: location of all json files
    @type blank_html: str
    @param blank_html: name of the blank HTML file
    @type unit_html: str
    @param unit_html: name of the unit HTML file
    """
    # Get all json file in this dir
    json_list = []
    for filename in os.listdir(json_dir):
        if filename.endswith(".json"):
            json_list.enpand(os.path.join("json", filename))
    # Save all those data to a dict
    json_info = {}
    for json_file in json_list:
        with open(os.path.join(json_dir, json_file), "r") as jsonFile:
            json_info[json_file[:-5]] = json.load(jsonFile)

    # Fill unit and save to html_info dict
    html_info = {}
    with open(unit_html, "r") as unitHTML:
        unit_soup = BeautifulSoup(unitHTML.read(), 'lxml')
    for user, json_data in json_info:
        for name_of_id, value_of_id in json_data.items():
            id = unit_soup.find(attrs={"id": name_of_id})
            id.string = str(value_of_id)
        html_info[user] = unit_soup.prettify()

    with open(blank_html, "r") as blankHTML:
        blank_soup = BeautifulSoup(blankHTML.read(), 'lxml')


if __name__ == '__main__':

fill_html("json")
