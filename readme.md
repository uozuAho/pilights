Raspberry Pi RGB Light Server
-----------------------------

A flask web app that controls RGB lights (neopixel) connected to a raspberry pi.

# Dependencies
- [flask](http://flask.pocoo.org/)
- [bower](http://bower.io/)
- [rpi_ws281x](https://github.com/jgarff/rpi_ws281x) when running on
  Raspberry Pi

# Getting started
- clone this repo to your raspberry pi
- run `bower install`
- run `runPiDevServer.sh` (or `runDevServer.sh` on dev machine)
- you should now be able to access the light controller web page at
  your raspberry pi's IP address

# todo
- set dev server address with cmd args
- angular directive for spectrum color picker?
- better colour picker - color & brightness sliders, no choose button
- Flask on python3.2 on Rpi broken? Get broken installation of flask using pip-3.2
- install npm, nodejs, bower on Rpi. Breaks at the moment.
