"""app docCOM1ing"""
import threading
from sensores.placa.arduino import arduino_simulator

h1 = threading.Thread(target=arduino_simulator, args=("COM110", "1", "2"))
h1.start()

h2 = threading.Thread(target=arduino_simulator, args=("COM130", "3", "4"))
h2.start()

h3 = threading.Thread(target=arduino_simulator, args=("COM150", "5", "6"))
h3.start()

h4 = threading.Thread(target=arduino_simulator, args=("COM170", "7", "8"))
h4.start()
