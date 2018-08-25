Raspberry Pi RGB Light Server
-----------------------------

A flask web app that controls RGB lights (neopixel)


# Required hardware

- neopixel strip
- neopixel driver hardware - see pi_pixels and/or arduino_pixels
- 5v PSU with enough capacity to drive all LEDs (I think each pixel is ~60mA max)


# Getting started

To run the web app on a dev machine:

```
sudo apt-get install python  # you've probably already got this. Make sure it's python 2.7.x
sudo pip install flask
npm install -g bower
bower install
python flask-app.py
```

If the hardware neopixel library is not found, the web app will use a mock neopixel
object for testing, which outputs LED data to the console. You should now be able to
open localhost:5000 in your browser & see a colour picker.

If running on the raspberry pi, sudo is required for hardware access to drive LEDs,
and use --host 0.0.0.0 to allow external connections:

    sudo python flask-app.py --host 0.0.0.0

You should now be able to access the light controller web page at your raspberry
pi's IP address.
