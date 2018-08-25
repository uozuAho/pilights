# arduino code

Arduino neopixel controller. Listens for pixel values on the serial port.

# Dependencies

- Arduino IDE (tested with 1.8.5)
- Arduino compatible board (tested with Uno)
- Adafruit NeoPixel library (https://github.com/adafruit/Adafruit_NeoPixel)
- VS Code (optional IDE) + Microsoft arduino extension

# Getting started - hardware

- As per Adafruit 'strandtest' example sketch
    + NeoPixel strip connected to pin 6

# Getting started - software

- Open this directory in VS Code
- You may need to correct the library/browse dirs in .vscode/c_cpp_properties.json
- Set the arduino serial port via command palette -> Arduino: Select Serial Port
- Use the command palette to select Arduino: Upload. This will build and upload the
  software to your arduino

You should be able to verify + upload this code using the Arduino IDE (untested).
