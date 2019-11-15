import serial
import random

from time import sleep

from ..db.config import PYSERIAL_DELAY_ARDUINO


def arduino_simulator(portcom, sensora, sensorb):
    
    ser = serial.Serial(portcom, 9600)

    while True:
        t = random.randint(35, 50)
        h = random.randint(1, 100)

        data = dict(T=str(t), H=str(h), sensorT=sensora, sensorH=sensorb)

        message = str(data) + "\n"
        ser.write(message.encode("raw_unicode_escape"))
        print(message)
        sleep(PYSERIAL_DELAY_ARDUINO)

    ser.close()
