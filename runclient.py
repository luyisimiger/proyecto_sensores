"""app docCOM1ing"""
import threading
from sensores.client.client import receiver
from sensores.db import util

util.conectdb()
r = util.connect_redis()

h1 = threading.Thread(target=receiver, args=("COM120", "1", "2", r))
h1.start()

h2 = threading.Thread(target=receiver, args=("COM140", "3", "4", r))
h2.start()

h3 = threading.Thread(target=receiver, args=("COM160", "5", "6", r))
h3.start()

h4 = threading.Thread(target=receiver, args=("COM180", "7", "8", r))
h4.start()
