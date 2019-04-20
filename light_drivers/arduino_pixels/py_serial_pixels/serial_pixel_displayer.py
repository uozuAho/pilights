import serial
import time

NUM_LEDS = 43


class SerialPixelDisplayer: # implements Displayer
    def __init__(self, generator_func, port='/dev/ttyACM0', baud=57600):
        self.generate = generator_func
        self.port = port
        self.baud = baud

    def run(self):
        with _SerialPixels(self.port, self.baud) as strip:
            while True:
                pixels = self.generate()
                strip.set(pixels)
                time.sleep(0.02)

    def are_pixel_vals_same(self, pixels1, pixels2):
        if len(pixels1) != len(pixels2):
            return False
        for p1, p2 in zip(pixels1, pixels2):
            if p1.rgb[0] != p2.rgb[0]: return False
            if p1.rgb[1] != p2.rgb[1]: return False
            if p1.rgb[2] != p2.rgb[2]: return False
        return True

    def dispose(self):
        pass


class _SerialPixels:
    """ serial led strip interface, supporting Generator interface """
    def __init__(self, port, baud, brightness_limit=255):
        self.STOP_BYTE = 255
        self.serial = serial.Serial(port, baud)
        self.brightness_limit = brightness_limit
        self.current_rgb_vals = None

    def __enter__(self):
        return self

    def __exit__(self, type, val, trace):
        self.dispose()

    def dispose(self):
        if self.serial:
            self.serial.close()

    def set(self, pixels):
        """ Set leds with pixel values
            Parameters:
                pixels: array of presenter.Pixel
        """
        rgb_array = [int(x) for pixel in pixels for x in pixel.rgb]
        if self._are_rgb_arrays_equal(rgb_array, self.current_rgb_vals):
            # if led values are the same, don't bother sending. This stops
            # spamming the serial port when nothing's happening... dunno if that's necessary,
            # but it keeps me up at night.
            return
        self.current_rgb_vals = rgb_array
        self._check_values(rgb_array)
        self._set_leds(rgb_array)

    def _check_values(self, rgb_array):
        """ Ensure values are <= max brightness and != stop byte """
        for i, value in enumerate(rgb_array):
            if value > self.brightness_limit:
                rgb_array[i] = self.brightness_limit
            if value == self.STOP_BYTE:
                rgb_array[i] -= 1

    def _are_rgb_arrays_equal(self, arr1, arr2):
        if not arr1 or not arr2:
            return False
        if len(arr1) != len(arr2):
            return False
        for a1, a2 in zip(arr1, arr2):
            if a1 != a2:
                return False
        return True

    def _set_leds(self, rgb_array):
        self.serial.write(bytes(list(rgb_array) + [self.STOP_BYTE]))

    def close(self):
        self.serial.close()
