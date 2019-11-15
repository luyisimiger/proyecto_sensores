"""modulo con rutinas de utilidad para el manejo de la base de datos"""

import redis
from mongoengine import * # pylint: disable=all
from . import config
from .managers import SensorManager


def conectdb():
    return connect(config.MONGODB_DATABASE)

def connect_redis():
    return redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, password=config.REDIS_PASSWORD)
