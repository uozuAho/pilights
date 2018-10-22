from threading import Thread

from pixel_generator_slave import PixelGeneratorSlave


class PixelService:
    """ Deals with all pixel stuff required by the flask app """
    def __init__(self, num_pixels):
        self.pixelgen = PixelGeneratorSlave(num_pixels)

    def start_displayer(self, device):
        if device == 'pygame':
            from pygame_pixels.pygame_pixels import PygamePixelDisplayer
            pixeldisp = PygamePixelDisplayer(self.pixelgen.generate)
        elif device == 'arduino':
            from arduino_pixels.py_serial_pixels.serial_pixel_displayer import SerialPixelDisplayer
            pixeldisp = SerialPixelDisplayer(self.pixelgen.generate)
        else:
            raise Exception('unknown displayer device: ' + device)

        # run the displayer in a background thread, since it runs a blocking loop
        dispthread = Thread(target=pixeldisp.run)
        dispthread.start()

    def set_all(self, r, g, b):
        self.pixelgen.set_all(r, g, b)
