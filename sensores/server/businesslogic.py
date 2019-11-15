from sensores.db.models import Sensor, Medition

from . import todict


def get_sensor_data(sensor, meditions=None):

    if meditions is None:
        meditions = Medition.objects(sensor=sensor.id)

    return todict.sensor(sensor, meditions)


def get_sensors_data():

    sensores = []

    for s in Sensor.objects:
        sensor = get_sensor_data(s)
        sensores.append(sensor)

    return dict(sensores=sensores)
