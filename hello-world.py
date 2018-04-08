from flask import Flask
from helpers.middleware import setup_metrics
import prometheus_client

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

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

@application.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    application.run()
