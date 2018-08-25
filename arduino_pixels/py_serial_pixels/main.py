from contextlib import contextmanager
import serial
import time

NUM_LEDS = 43

@contextmanager
def led_manager(serial_led):
    led = serial_led
    try:
        yield led
    except:
        led.close()
        raise
    else:
        led.close()

class SerialLed:
    """ serial led strip interface """
    def __init__(self, port, baud, num_leds):
        self.serial = serial.Serial(port, baud)
        self.num_leds = num_leds

    def set(self, strip):
        """ Set leds with LedStrip values """
        rgb_array = [int(x) for color in strip.leds for x in color.get_rgb()]
        self._set_leds(rgb_array)

    def _set_leds(self, rgb_array):
        self.serial.write(bytes(list(rgb_array) + [255]))

    def close(self):
        self.serial.close()

class Color:
    def __init__(self, r=0, g=0, b=0):
        self.set_rgb(r, g, b)

    def get_rgb(self):
        return self.r, self.g, self.b

    def set_rgb(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def set_color(self, color):
        self.r = color.r
        self.g = color.g
        self.b = color.b

    def clear(self):
        self.set_rgb(0, 0, 0)

class LedStrip:
    def __init__(self, num_leds):
        self.leds = [Color() for i in range(num_leds)]

    def clear(self):
        for led in self.leds:
            led.clear()

class LedStripBlob:
    """ moves a 'blob' of light on the led strip """
    def __init__(self, num_leds):
        self.num_leds = num_leds
        self.pos = 0
        # LEDs per second in positive LED direction
        self.speed = 0
        self._time_last = time.time()

    def update(self, time_s):
        """ update blob state """
        dt = time_s - self._time_last
        self._time_last = time_s
        self.pos += self.speed * dt
        # stay in led range
        if self.pos < 0:
            self.pos += self.num_leds
        if self.pos > self.num_leds:
            self.pos -= self.num_leds

    def render(self, strip):
        """ render self onto given LED strip """
        pos = int(self.pos)
        strip.leds[pos].set_rgb(10, 10, 10)

class LedStripRainbowCycle:
    """ cycle rainbow ... yeah """
    def __init__(self):
        self.color_defs = [
            Color(100, 0, 0),
            Color(0, 100, 0),
            Color(0, 0, 100)
        ]
        self.leds = [Color() for i in range(NUM_LEDS)]
        # target color_defs idx per led
        self.targets = [0 for i in range(NUM_LEDS)]
        # brightness notches per second
        self.speed = 50
        self._time_last = time.time()

    def increment_single_led(self, color, target_color, dt):
        pass

    def increment_single_color(self, c, target, dt):
        """ get value to increment a single color (ie r, g or b) """
        sign = 1 if c < target else -1
        dc = int(dt * self.speed)
        if abs(c - target) < abs(dc):
            dc = abs(c - target)
        return sign * dc

class Thing:
    def __init__(self):
        self.color = Color()
        self.speed = 25
        self._time_last = time.time()
        self.maxb = 50

    def update(self):
        dt = time.time() - self._time_last
        self._time_last = time.time()
        dc = dt * self.speed
        def calc_new_val(c):
            if c == self.maxb:
                return self.maxb
            return min(c + dc, self.maxb)
        if self.color.r < self.maxb:
            self.color.r = calc_new_val(self.color.r)
        elif self.color.g < self.maxb:
            self.color.g = calc_new_val(self.color.g)
        elif self.color.b < self.maxb:
            self.color.b = calc_new_val(self.color.b)
        else:
            self.color.clear()

    def render(self, strip):
        for led in strip.leds:
            led.set_color(self.color)


with led_manager(SerialLed('/dev/ttyACM0', 57600, NUM_LEDS)) as led:
    strip = LedStrip(NUM_LEDS)
    blob = LedStripBlob(NUM_LEDS)
    blob.speed = 43
    thing = Thing()
    while True:
        blob.update(time.time())
        thing.update()
        strip.clear()
        thing.render(strip)
        blob.render(strip)
        led.set(strip)
        time.sleep(0.02)