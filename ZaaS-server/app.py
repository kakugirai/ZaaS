import os
import time

from flask import Flask, json, request

app = Flask(__name__)

@app.route('/zanryu', methods = ['POST'])
def api_message():
    if request.headers['Content-Type'] == 'application/json':
        # Read request
        data = request.json
        # Save different types of data to different dirs
        dir_today = time.strftime("%m-%d-%Y")
        dirs = ["json", "html", "pdf"]
        # Create dir if not exists
        for dirname in dirs:
            if not os.path.exists(os.path.join(dirname, dir_today)):
                os.makedirs(os.path.join(dirname, dir_today))
        # Deprive login name in data
        data_without_login_name = {key: value for key, value in data.items() if value is not data["login_name"]}
        # Wirte json file
        with open(os.path.join("json", dir_today, data["login_name"] + ".json"), "w+") as json_file:
            json_file.write(json.dumps(data_without_login_name))
            # Write html file
            with open(os.path.join("html", dir_today, data["login_name"] + ".html"), "w+") as config:
                html_file.write(fill_html(json_file))
        # print data["login_name"] + ".json created"
        return data["login_name"] + ".json created"
    else:
        return "415 Unsupported Media Type"

if __name__ == '__main__':
    app.run()

