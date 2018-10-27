RGB Light Server
----------------

Flask-based web server to run connected neopixels.


# Getting started

Install requirements:

    sudo apt-get install python3-flask

To run:

    python3 flask-app.py --host 0.0.0.0 --device arduino

You should now be able to control the arduino-connected neopixels from http://<machine ip>:5000/


# Run on startup

To run the server on startup, add the following line to /etc/rc.local:

    python3 /path/to/your/pilights/flask_pixel_server/flask-app.py --host 0.0.0.0 --device arduino &
