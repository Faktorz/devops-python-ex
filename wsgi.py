from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello New World!"

@application.route("/test")
def hello():
    return "This is a test!"

if __name__ == "__main__":
    application.run()
