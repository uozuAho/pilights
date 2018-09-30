# These interfaces are used by the presenter (sort of)

class Pixel:
    """ An RGB pixel """
    def __init__(self):
        self.rgb = [0, 0, 0]

class Generator:
    def generate(self, time):
        """ Generate an array of pixels

        Parameters:
            time: float: time since last call, in milliseconds

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
            generate: (time: float (s)) => Array(Pixel)
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
