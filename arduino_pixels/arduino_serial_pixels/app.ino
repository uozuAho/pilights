#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define NUM_LEDS 43

// data output pin to neopixels (arduino pin number)
#define NEOPIX_OUT_PIN 6

const int RECV_BUF_SIZE = NUM_LEDS * 3;

uint8_t recv_buf[RECV_BUF_SIZE];
// current recv buf idx
int bufidx = 0;
// leds ready to update?
bool update_leds = false;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, NEOPIX_OUT_PIN, NEO_GRB + NEO_KHZ800);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.

void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  Serial.begin(57600);
}

void loop() {
  recvBytes();

  if (update_leds) {
    update_leds = false;
    for (int i = 0; i < NUM_LEDS; i++) {
      int i3 = i * 3;
      uint8_t r = recv_buf[i3];
      uint8_t g = recv_buf[i3 + 1];
      uint8_t b = recv_buf[i3 + 2];
      strip.setPixelColor(i, r, g, b);
    }
    strip.show();
  }
}

void recvBytes() {
  int b = 0;
  while (1) {
    b = Serial.read();
    // -1 means no bytes in serial buffer
    if (b == -1) break;
    if (b == 255) {
      // 255 is 'stop' byte
      bufidx = 0;
      update_leds = true;
      break;
    }
    if (bufidx < RECV_BUF_SIZE) {
      recv_buf[bufidx++] = (uint8_t) b;
    }
  }
}
