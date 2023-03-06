from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", data=readJson("config.json"))


def readJson(path):
    with open(path) as f:
        return json.load(f)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
