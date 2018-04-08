from flask import Flask, Response
from middleware import setup_metrics
import prometheus_client

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

application = Flask(__name__)
setup_metrics(application)

@application.route("/")
def hello():
    return "Hello New World!"

@application.route("/test")
def test():
    return "This is a test!"

@application.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    application.run()
