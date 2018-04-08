from flask import Flask
from middleware import setup_metrics

application = Flask(__name__)

setup_metrics(application)

@application.route("/")
def hello():
    return "Hello World!"

@application.route('/test/')
def test():
    return 'rest'

@application.route('/test1/')
def test1():
    1/0
    return 'rest'

@application.errorhandler(500)
def handle_500(error):
    return str(error), 500

if __name__ == "__main__":
    application.run()
