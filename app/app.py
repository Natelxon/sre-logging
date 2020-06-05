from flask import Flask, render_template
import os
import threading

from statsrunner import StatsRunner

app = Flask(__name__)


@app.route('/')
def index():
    return ""


# Get stats
@app.route('/stats')
def stats():
    return statistics.summary()


if __name__ == "__main__":
    logfile = os.environ['LOG_FILE']
    statistics = StatsRunner(logfile)

    # Start log monitor in the background
    thread = threading.Thread(target=statistics.analyze)
    thread.start()

    app.run(host='0.0.0.0', port=8080)
