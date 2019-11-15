
import json
import serial
import random

from datetime import datetime
from time import sleep

from ..db import config
from ..db.models import Sensor, Medition


def make_json_data(medition):

    json_data = json.dumps({
        "sensor": {
            "name": medition.sensor.name
        },
        'time': medition.fechahora.strftime('%Y-%m-%d %H:%M:%S'),
        'value': medition.value
    })

    return json_data


def process_medition(s, v, redis_client):
    f = datetime.now()
    m = Medition(sensor=s, fechahora=f, value=v)
    m.save()

    redis_client.publish(config.REDIS_CHANNEL_REALTIME, make_json_data(m))

    return m

def receiver(portcom, sensora, sensorb, redis_client):
    ser = serial.Serial(portcom, 9600)
    sa = Sensor.objects(code=sensora).first()
    sb = Sensor.objects(code=sensorb).first()

    while True:
        message = ser.readline()
        msg = message.decode("utf-8").replace("'", "\"")
        data = json.loads(msg)

        med1 = process_medition(sa, int(data["T"]), redis_client)
        med2 = process_medition(sb, int(data["H"]), redis_client)

        # x = json.dumps(med1)
        print(med1, med2)

        sleep(config.PYSERIAL_DELAY)

    ser.close()
