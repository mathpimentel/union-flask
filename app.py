from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/about")
def about():
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True, port=8000)