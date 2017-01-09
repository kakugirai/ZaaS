from flask import Flask, json, request

app = Flask(__name__)

@app.route('/zanryu', methods = ['POST'])
def api_message():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        with open(data["login_name"] + ".json", "w+") as config:
            config.write(json.dumps(data))
        print data["login_name"] + ".json created"
        return data["login_name"] + ".json created"
    else:
        return "415 Unsupported Media Type"

if __name__ == '__main__':
    app.run()

