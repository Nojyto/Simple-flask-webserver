from flask import Flask, render_template

cfg = {
    "name": "Kodo gavimas",
    "code": "1123123",
    "img": "https://picsum.photos/300/600"
}


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", data=cfg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
