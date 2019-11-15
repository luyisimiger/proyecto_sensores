"""server docstring"""
import json

from datetime import datetime
from sensores.db.models import Sensor, Medition
from .application import application as app
from .businesslogic import get_sensors_data

@app.route('/data')
def data():
    return get_sensors_data()
