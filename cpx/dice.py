from adafruit_circuitplayground import cp
import random
import time

while True:
    if cp.button_a:
        cp.pixels.fill((0, 0, 0))
        dice = random.randint(0, 10)
        for i in range(0, dice):
            cp.pixels[i] = ((0, 0, 255))
        time.sleep(.4)
    if cp.button_b:
        cp.pixels.fill((0, 0, 0))