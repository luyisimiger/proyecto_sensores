import json
import random
import time

from datetime import datetime, timedelta
from flask import Flask, Response, render_template, redirect, url_for
from flask import Blueprint
from mongoengine import Q

from sensores.db.models import Sensor, Medition
from sensores.server import todict
from .application import redis_client
from .businesslogic import get_sensor_data
from ..db.config import REDIS_CHANNEL_REALTIME
from ..db.managers import MeditionManager as mManager


sensor = Blueprint('sensor', __name__)


@sensor.route('/sensors')
def sensors_list():
    sensors = Sensor.objects
    return render_template('sensors/list.html', sensors=sensors)

@sensor.route('/sensors/<code>')
def sensors_detail(code):
    s = Sensor.objects(code=code).first()
    meditions = Medition.objects(sensor=s.id)
    meditions_general = mManager.get_meditions_by_sensor_type(s.type)
    medition_pico = Medition.objects(sensor=s.id).order_by('-value').first()
    
    ctx = {
        'sensor': s,
        'meditions': meditions,
        'data': get_sensor_data(s, meditions),
        'data_general': todict.meditions(meditions_general),
        'medition_pico': medition_pico
    }
    return render_template('sensors/detail.html', **ctx)

@sensor.route('/sensors/<code>/grafica')
def sensors_grafica(code):
    s = Sensor.objects(code=code).first()
    meditions = Medition.objects(sensor=s.id)
    meditions_general = mManager.get_meditions_by_sensor_type(s.type)
    medition_pico = Medition.objects(sensor=s.id).order_by('-value').first()
    
    ctx = {
        'sensor': s,
        'meditions': meditions,
        'data': get_sensor_data(s, meditions),
        'data_general': todict.meditions(meditions_general),
        'medition_pico': medition_pico
    }

    return render_template('sensors/grafica.html', **ctx)
