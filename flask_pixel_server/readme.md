Raspberry Pi RGB Light Server
-----------------------------

Rewrite of flask_pixels. No bower, no angular.


# Getting started

Install requirements:

    sudo apt-get install python3-flask

If running on the raspberry pi, use --host 0.0.0.0 to allow external connections:

    python3 flask-app.py --host 0.0.0.0

You should now be able to access the light controller web page at your raspberry
pi's IP address.
