# Raspberry Pi RGB Light Server
-------------------------------

Various ways to control neopixels (RGB LEDs), including a web app which can be run
on a raspberry pi.


# Quick start

Demo the LED patterns on a PC:

    python3 pixel_patterns/demo.py

Host a web app that controls connected pixels (or pygame-emulated pixels):

    cd flash_pixel_server
    python3 flask-app.py
    # goto localhost:5000 to control pixels


# Directory structure

discovery_client/
    - discover other pilights on the local network

flask_pixel_server/
    - flask web app to control all the pixels

light_drivers/
    - control various light hardware, eg neopixels, pygame renderer
    - go here to add & test your own device. drivers should implement the 'Displayer' interface

pixel_patterns/
    - RGB strip patterns that can be used anywhere
    - use `demo.py` in here to test out patterns on your device


# todo

- discovery: 'client' the wrong word? what about friends?
- discovery: integrate with flask server?
- run on pi startup. rc.local not working. why? no logs.
- touch-friendly RGB sliders in flask app
- get more patterns from neogoggles
