"""populate random meditions"""

from datetime import datetime, timedelta
from sensores.db import util
from sensores.db.models import Sensor
from sensores.db.managers import MeditionManager


if __name__ == "__main__":
    # pylint: disable=invalid-name

    delta = timedelta(days=1)
    dateini = datetime(2019, 11, 1)
    datefin = datetime.today()
    d = dateini

    util.conectdb()

    while d <= datefin:
        print("process", d)
        for sensor in Sensor.objects: # pylint: disable=no-member
            # MeditionManager.delete_meditions(sensor)
            MeditionManager.populate_data(sensor, d)

        d = d + delta
