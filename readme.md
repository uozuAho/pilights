Raspberry Pi RGB Light Server
-----------------------------

A flask web app that controls RGB lights (neopixel) connected to a raspberry pi.

Thanks to:
- https://github.com/jgarff/rpi_ws281x
- https://learn.adafruit.com/neopixels-on-raspberry-pi/software


# Required hardware

- raspberry pi (tested with version 3)
- 3v3 to 5v level shifter (there's ways around this which I won't go into)
    * This project uses https://www.pololu.com/product/2595
- 5v PSU with enough capacity to drive all LEDs (I think each pixel is ~60mA max)


# Getting started - non-pi dev machine

You can run the web app on a development machine. It will use a mock neopixel object
for testing, which outputs LED data to the console.

```
sudo apt-get install python  # you've probably already got this. Make sure it's python 2.7.x
sudo pip install flask
npm install -g bower
bower install
./runDevServer.sh
```

You should now be able to open localhost:5000 in your browser & see a colour picker.

-------------------------------------------------------------------------------
# Getting started - pi

## Disable audio
- create a file /etc/modprobe.d/snd-blacklist.conf with a single line

blacklist snd_bcm2835

- use `sudo raspi-config` to force audio through HDMI
- reboot
- confirm that the soundcard is disabled by running `aplay -l`. You should see

    aplay: device_list:268: no soundcards found...

## Connect hardware

- 5v supply to HV in of level shifter
- pi pin 1 to LV in of level shifter
- pi pin 12 to LV 1 of level shifter (through resistor?)
- HV 1 of level shifter to LED data in

Note that the neopixel library data output is on pin 12 (not 18!) by default. The adafruit
demos say 'pin 18', but they mean GPIO 18, which is on pin 12.

## Build rpi_ws281x/neopixel library

```
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig
# clone & build library
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
# install to python libraries
cd python
sudo python setup.py install
```

You should now be able to test the LEDs (assuming all hardware is connected).

`cd examples`, then modify config at the top of strandtest.py to your liking.
Assuming your setup is as per everything above, on a fresh raspbian installation
on a raspberry pi 3, you probably just need to change LED_COUNT. Also maybe
turn down LED_BRIGHTNESS to prevent blinding yourself :)

Now run `sudo python strandtest.py`. You should see some demo patterns on the
LEDs.

## Run this project's web server

Now everything's ready to host the server.

```
sudo apt-get install python-flask
git clone https://github.com/uozuAho/pilights  # this project
cd pilights
bower install
sudo runPiDevServer.sh
```

You should now be able to access the light controller web page at your raspberry
pi's IP address.


-------------------------------------------------------------------------------
# todo
- set dev server address with cmd args
- better colour picker - color & brightness sliders, no choose button
