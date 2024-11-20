from adafruit_circuitplayground import cp
import time

while True:
    for i in range(0,10):
        cp.pixels[i] = ((255, 0, 0))
        if i == 9:
            cp.play_tone(500, .5)
            cp.pixels.fill((0, 0, 0))
    for i in range(0,10):
        cp.pixels[i] = ((0, 0, 255))
        if i ==  9:
            cp.play_tone(900, .5)
            cp.pixels.fill((0, 0, 0))
