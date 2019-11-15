import json
import random
import time

from datetime import datetime
from flask import Flask, Response, render_template, redirect, url_for
from flask import Blueprint

from sensores.db.models import Sensor # Medition
from .application import redis_client
from .businesslogic import get_sensors_data
from ..db.config import REDIS_CHANNEL_REALTIME


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for("main.realtime"))

@main.route('/realtime')
def realtime():
    data = get_sensors_data()
    return render_template('realtime.html', data=data)

@main.route('/chart-data')
def chart_data():
    pubsub = redis_client.pubsub()
    pubsub.subscribe(REDIS_CHANNEL_REALTIME)

    def generate_random_data():
        for message in pubsub.listen():
            
            if message["type"] != "message":
                continue

            json_data = message["data"].decode("utf-8")
            print(json_data)

            yield f"data:{json_data}\n\n"

    return Response(generate_random_data(), mimetype='text/event-stream')
