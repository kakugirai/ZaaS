 # -*- coding: utf-8 -*-
import json
from datetime import date
from bs4 import BeautifulSoup

tmp = {
    "student-id": "",
    "gakubu": "",
    "gakunen": "",
    "student-name": "",
    "class-name": "",
    "teacher-name": "",
    "location": "",
    "parent-name": "",
    "relation": "",
    "tele": ""
}

def fill_date(file_name):
    i = date.today()
    weekdays = ["月", "火", "水", "木", "金", "土", "日"]
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
        data["year"] = i.year
        data["month"] = i.month
        data["day"] = i.day
        data["weekday"] = weekdays[i.weekday()]
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file)
    return

def fill_html(html_file, json_file):
    with open(html_file, "r", encoding="utf-8") as htmlFile:
        soup = BeautifulSoup(htmlFile.read(), 'lxml')
    with open(json_file, "r", encoding="utf-8") as jsonFile:
        data = json.load(jsonFile)
    for row in soup.find_all(attrs={"class": "col-1-2"}):
        for key, value in data.items():
            id = row.find(attrs={"id": key})
            id.string = str(value)
    html = soup.prettify()
    with open("zanryu.html", "w+", encoding="utf-8") as htmlFile:
        htmlFile.write(html)


if __name__ == '__main__':
    fill_date("info/guo.json")
    fill_html("blank.html", "info/guo.json")
