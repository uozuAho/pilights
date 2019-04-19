# Raspberry Pi RGB Light Server
-------------------------------

Various ways to control neopixels (RGB LEDs), including a web app which can be run
on a raspberry pi.


# Quick start

Demo the LED patterns on a PC:

    python3 demo.py

Host a web app that controls connected pixels (or pygame-emulated pixels):

    cd flash_pixel_server
    python3 flask-app.py
    # goto localhost:5000 to control pixels


# Directory structure

arduino_pixels/
    - Control neopixels with an arduino. Contains arduino 'serial slave' firmware + serial host
      app written in python.

discovery_client/
    - discover other pilights on the local network

flask_pixel_server/
    - flask web app to control all the pixels

phat_pixels/
    - Control a Pimoroni pHAT

pi_pixels/
    - Control neopixels with a raspberry pi, using the pi's IO pins.

pixel_patterns/
    - neopixel strip patterns that can be used anywhere

pygame_pixels/
    - emulate pixels on the screen, using pygame


# todo

- discovery: 'client' the wrong word? what about friends?
- discovery: integrate with flask server?
- run on pi startup. rc.local not working. why? no logs.
- touch-friendly RGB sliders in flask app
- get more patterns from neogoggles
