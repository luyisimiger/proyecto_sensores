"""app docstring"""

from sensores.server import app

app.run(host='0.0.0.0', debug=True, threaded=True)
