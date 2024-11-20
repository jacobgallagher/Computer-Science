from adafruit_circuitplayground import cp
import time
import random

while True:
    x, y, z = cp.acceleration
    if abs(y) >= 15 or abs(x) >= 15:
        for i in range(0,10):
            r = random.randint (0,125)
            g = random.randint(0,125)
            b = random.randint(0,125)
            cp.pixels[i] = ((r, g, b))
        time.sleep(.2)
