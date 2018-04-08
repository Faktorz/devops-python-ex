import os
from flask import Flask, Response
from prometheus_client import multiprocess
from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST, Gauge, Counter

application = Flask(__name__)

IN_PROGRESS = Gauge("inprogress_requests", "Example gauge", multiprocess_mode='livesum')
NUM_REQUESTS = Counter("num_requests", "Example counter")


@application.route("/")
@IN_PROGRESS.track_inprogress()
def hello():
    NUM_REQUESTS.inc()
    return "Hello World from {}!".format(os.getpid())


@application.route("/metrics")
def metrics():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    application.run()
