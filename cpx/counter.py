from adafruit_circuitplayground import cp
import random
import time
n = 0
while True:
    if cp.button_a:
        
        n = n + 1
        for i in range(0, n):
            cp.pixels[i] = ((0, 0, 255))
        if n == 10:
            n = 9
        time.sleep(.25)
    if cp.button_b:
        if n == 10:
            n = 9
        cp.pixels[n] = ((0, 0, 0))
        n = n - 1
        time.sleep(.25)