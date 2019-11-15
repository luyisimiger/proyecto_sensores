from mongoengine import * # pylint: disable=all

class Sensor(Document):
    code = StringField(required=True)
    name = StringField(required=True)
    type = StringField(required=True, max_length=20)

    def __repr__(self):
        return f"{self.code} - {self.name}, {self.type}"

    def __str__(self):
        return self.__repr__()


class Medition(Document):
    sensor = ReferenceField(Sensor, required=True, reverse_delete_rule=2)
    fechahora = DateTimeField(required=True)
    value = FloatField(required=True)

    def __repr__(self):
        return f"{self.sensor.__repr__()}, {self.fechahora}, {self.value}"

    def __str__(self):
        return self.__repr__()
