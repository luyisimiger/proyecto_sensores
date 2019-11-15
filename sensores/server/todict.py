from sensores.db.models import Sensor, Medition


def medition(m):
    return {
        'fechahora': m.fechahora.strftime('%Y-%m-%d %H:%M:%S'),
        'value': m.value
    }


def meditions(lmeditions):
    
    _meditions = []

    for m in lmeditions:
        _meditions.append({
            'fechahora': m.fechahora.strftime('%Y-%m-%d %H:%M:%S'),
            'value': m.value
        })
    
    return _meditions


def sensor(s, lmeditions=None):
    return {
        'type': s.type,
        'code': s.code,
        'name': s.name,
        'meditions': meditions(lmeditions)
    }


def sensors(lsensors):

    _sensors = []

    for s in Sensor.objects:
        sensor = sensor(s)
        _sensors.append(sensor)

    return _sensors
