import random
from datetime import datetime, time
from .models import Sensor, Medition

class SensorManager:
    """SensorManager"""

    @staticmethod
    def create_sensors():
        """registra los sensores en la base de datos"""

        types = ["Temperatura", "Humedad"]

        for i in range(1, 9):
            name = f"Sensor No. {i}"
            sensor = Sensor(code=str(i), name=name, type=random.choice(types))
            sensor.save()

    @staticmethod
    def delete_sensors():
        """elimina los sensores registrados en la base de datos"""

        for sensor in Sensor.objects: # pylint: disable=no-member
            sensor.delete()

    @staticmethod
    def recreate_sensors():
        """recreate_sensors"""

        SensorManager.delete_sensors()
        SensorManager.create_sensors()



class MeditionManager:
    """MeditionManager"""

    @staticmethod
    def populate_data(s, d): # pylint: disable=invalid-name
        """populate_data"""

        for hour in range(0, 24):

            if s.type == "Temperatura":
                value = random.randrange(18, 33)
            else:
                value = random.randrange(0, 99)

            tm = time(hour)
            fechahora = datetime.combine(d, tm)
            medition = Medition(sensor=s, fechahora=fechahora, value=value)
            medition.save()

    @staticmethod
    def delete_meditions(s): # pylint: disable=invalid-name
        """delete_meditions"""

        for medition in Medition.objects(sensor=s.id):
            medition.delete()
    
    @staticmethod
    def get_meditions_by_sensor_type(stype): # pylint: disable=invalid-name
        """get_meditions_by_sensor_type"""

        sensors = Sensor.objects(type=stype)
        medition = Medition.objects(sensor__in=sensors)

        return medition
