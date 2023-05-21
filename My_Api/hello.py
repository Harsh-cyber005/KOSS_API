from flask import Flask

app = Flask(__name__)


@app.route("/")
def func():
    return "Harsh Guptaaa"


@app.route("/<name>")
def print_name(name):
    return "Hi, {}".format(name)


if __name__ == "__main__":
    app.run()
