# Raspberry Pi RGB Light Server
-------------------------------

Various ways to control neopixels (RGB LEDs), including a web app which can be run
on a raspberry pi.


# Quick start

Demo the LED patterns on a PC:

  python3 demo.py


# Directory structure

arduino_pixels/
  - Control neopixels with an arduino. Contains arduino 'serial slave' firmware + serial host
    app written in python.

flask_pixels/
  - flask web app to control all the pixels

pi_pixels/
  - Control neopixels with a raspberry pi, using the pi's IO pins.

pixel_patterns/
  - neopixel strip patterns that can be used anywhere

pygame_pixels/
  - emulate pixels on the screen, using pygame


# todo

- use patterns in flask_pixels
- get more patterns from neogoggles
