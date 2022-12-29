import time
from rpi_ws281x import PixelStrip, Color
import argparse

LED_COUNT = 6  # LED灯的个数pi4b2
LED_PIN = 21  # DI端接GPIO21

# 以下可以不用改
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53


# 以下为LED模式变换的各个函数
def colorWipe(strip, color, wait_ms=20):
    """一次擦除显示像素的颜色."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
    switch = "OFF"
    if switch == "OFF" :
       switch = input("if u want turn on the light input ON/OFF")
    if switch == "ON": 
   # while True:
       '''
        print('Color wipe animations.')
        colorWipe(strip, Color(255, 255, 0))  # Red wipe
        colorWipe(strip, Color(0, 0, 0), 30)
        colorWipe(strip, Color(0, 255, 255))  # Blue wipe
        colorWipe(strip, Color(0, 0, 0), 30)
        colorWipe(strip, Color(255, 0, 255))  # Green wipe
        colorWipe(strip, Color(0, 0, 0), 30)
       '''
       colorWipe(strip, Color(255, 229,204))
       while switch != "OFF":
             switch = input("turn off the light iput OFF//if u want change the light clor input C\n")
             if switch == "C":
                color_R = input("input Red value(0-255)\n")
                color_G = input("input Grenn value(0-255)\n")
                color_B = input("input Bule value(0-255)\n")
                R = int(color_R)
                G = int(color_G)
                B = int(color_B)
                colorWipe(strip, Color(R,G,B))
             elif switch == "OFF":
                  colorWipe(strip, Color(0, 0,0))
                  break

