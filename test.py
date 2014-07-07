from flask import Flask
yourflaskapp = Flask(__name__)

@yourflaskapp.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    yourflaskapp.run()
