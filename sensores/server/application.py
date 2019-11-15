"""server docstring"""

import json
import random
import time
from datetime import datetime
from flask import Flask, Response, render_template, redirect, url_for
from flask_mongoengine import MongoEngine

from sensores.db.models import Sensor, Medition
from sensores.db import util
from .businesslogic import get_sensors_data
from ..db.util import connect_redis

application = Flask(__name__)
application.config.from_object('sensores.server.config')
db = MongoEngine(application)

redis_client = connect_redis()

# register blueprint's
from .views import main as main_blueprint
from .sensors import sensor as sensor_blueprint

application.register_blueprint(main_blueprint)
application.register_blueprint(sensor_blueprint)

random.seed()  # Initialize the random number generator





@application.route('/stream/sensors/data')
def stream():
    def stream_sensors_data():

        for s in Sensor.objects:

            meditions = []

            for m in Medition.objects(sensor=s.id):
                meditions.append({
                    'fechahora': m.fechahora.strftime('%Y-%m-%d %H:%M:%S'),
                    'value': m.value
                })

            json_data = json.dumps({
                'sensor': {
                    'type': s.type,
                    'name': s.name,
                    'meditions': meditions
                }
            })

            yield f"data: {json_data}\n\n"
            time.sleep(0.6)

    return Response(stream_sensors_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    util.conectdb()
    application.run(debug=True, threaded=True)