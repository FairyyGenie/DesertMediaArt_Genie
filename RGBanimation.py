# this animation piece aims to examine the connection between colors, rhythm, and emotions
# through saying the same sentence in Morse Code 
# I wish to see how people would react to the animation emotionally 
# when the same messages is shown in different colors and speed of the rhythm

import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.2

# this says "Great"
Theline= "--. .-. . .- -"
colors = [ (255,69,0),(100,149,237), (138,43,226),(0,128,0)]

while True:

    # first speed : . for 0.3 - for 0.9 and space for 0.3
    # for loop through colors
    for c in colors:
        # for loop through messeges
        for x in Theline:
            print(x)
            if x == '.':
                led[0] = c
                time.sleep(0.3)
                
                led[0] = (0, 0, 0)
                time.sleep(0.05)
                
            elif x == '-':
                led[0] = c
                time.sleep(0.9)
                
                led[0] = (0, 0, 0)
                time.sleep(0.05)
            elif x == ' ':
                led[0] = (0,0,0)
                time.sleep(0.3)
                
                led[0] = (0, 0, 0)
                time.sleep(0.05)
         
        led[0] = (0, 0, 0)
        time.sleep(2)
        
    # second speed : . for 0.2 - for 0.6 and space for 0.2
     # for loop through colors
    for c in colors:
        # for loop through messeges
        for x in Theline:
            print(x)
            if x == '.':
                led[0] = c
                time.sleep(0.2)
                
                led[0] = (0, 0, 0)
                time.sleep(0.03)
                
            elif x == '-':
                led[0] = c
                time.sleep(0.6)
                
                led[0] = (0, 0, 0)
                time.sleep(0.03)
            elif x == ' ':
                led[0] = (0,0,0)
                time.sleep(0.2)
                
                led[0] = (0, 0, 0)
                time.sleep(0.03)
         
        led[0] = (0, 0, 0)
        time.sleep(2)
    
    # third speed : . for 0.5 - for 1.5 and space for 0.5
     # for loop through colors
    for c in colors:
        # for loop through messeges
        for x in Theline:
            print(x)
            if x == '.':
                led[0] = c
                time.sleep(0.5)
                
                led[0] = (0, 0, 0)
                time.sleep(0.06)
                
            elif x == '-':
                led[0] = c
                time.sleep(1)
                
                led[0] = (0, 0, 0)
                time.sleep(0.06)
            elif x == ' ':
                led[0] = (0,0,0)
                time.sleep(0.5)
                
                led[0] = (0, 0, 0)
                time.sleep(0.06)
         
        led[0] = (0, 0, 0)
        time.sleep(2)



