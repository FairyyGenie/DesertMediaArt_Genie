import time
import board
import analogio
import neopixel
import busio
import digitalio
import audioio
import audiomp3
import adafruit_lis3dh


pixel_pin = board.A3
num_pixels = 8

# Initialize analog input connected to photocell.
photocell = analogio.AnalogIn(board.A1)

# Make a function to convert from analog value to voltage.
def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False,
                           pixel_order=(1, 0 , 2, 3))



def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


RED = (255, 255, 255, 0)
YELLOW = (255, 150, 0, 0)
GREEN = (0, 255, 0, 0)
CYAN = (0, 255, 255, 0)
BLUE = (0, 0, 255, 0)
PURPLE = (20, 200, 25, 30)
Dark=(0,0,0,0)

while True:

    # Read the value, then the voltage.
    val = photocell.value
    volts = analog_voltage(photocell)
    # Print the values:
    print('Photocell value: {0} voltage: {1}V'.format(val, volts))

    if (val < 10000):
        pixels.fill(Dark)
        pixels.show()
    elif (val > 10000 and val < 25000):
        pixels.fill(CYAN)
        pixels.show()
    elif (val > 25000 and val < 30000):
        pixels.fill(PURPLE)
        pixels.show()
    elif (val >30000):
        pixels.fill(Dark)
        pixels.show()








