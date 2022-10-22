from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Folks!"

@app.route("/about")
def about():
    return "Hi my name is Aniruddh Singh"

if __name__ == "__main__":
    app.run()
