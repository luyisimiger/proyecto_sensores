"""docstring"""

import random
from mongoengine import * # pylint: disable=all
from sensores.db import util
from sensores.db.models import Sensor
from sensores.db.managers import SensorManager

if __name__ == "__main__":

    util.conectdb()
    SensorManager.recreate_sensors()
