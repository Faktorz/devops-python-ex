from flask import Flask
from middleware import setup_metrics

application = Flask(__name__)
setup_metrics(application)

@application.route("/")
def hello():
    return "Hello New World!"

@application.route("/test")
def test():
    return "This is a test!"

if __name__ == "__main__":
    application.run()
