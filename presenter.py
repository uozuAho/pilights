# 'interfaces' reference for neopixel pattern generators and displayers

class Pixel:
    """ An RGB pixel """
    def __init__(self, r=0, g=0, b=0):
        self.rgb = [r, g, b]

    def clear(self):
        self.rgb[0] = 0
        self.rgb[1] = 0
        self.rgb[2] = 0

    def copy_colour(self, pixel):
        self.rgb[0] = pixel.rgb[0]
        self.rgb[1] = pixel.rgb[1]
        self.rgb[2] = pixel.rgb[2]

class Generator:
    def generate(self):
        """ Generate an array of pixels

        Returns:
            Array(Pixel)
        """
        return []

class Displayer:
    def __init__(self, generate):
        """ Create the displayer with a method to generate pixels to display.
            generate is called internally by Displayer, since it knows when
            it's ready to display.

        Parameters:
            generate: () => Array(Pixel)
        """
        pass

    def set_generate(self, generate):
        """ Set the pixel generating function, as per the constructor """
        pass

    def run(self):
        """ Run the display loop """
        pass

class Presenter:
    """ Run a generator and displayer """
    def __init__(self, generator, displayer):
        self.generator = generator
        self.displayer = displayer
        self.displayer.set_generate(generator.generate)

    def run(self):
        self.displayer.run()
