from flask import Flask,render_template
import socket
import os

from statsrunner import StatsRunner

app = Flask(__name__)

@app.route('/stats')
def index():
    return statistics.summary()


if __name__ == "__main__":
    logfile = os.environ['LOG_FILE']

    statistics = StatsRunner(logfile)
    statistics.analyze()

    app.run(host='0.0.0.0', port=8080)