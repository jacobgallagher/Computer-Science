from adafruit_circuitplayground import cp
import random
import time

light = 0

while True:
    if cp.light == 30 or cp.light ==  29 or cp.light == 28:
        light = 0
    if cp.light == 27 or cp.light ==  26 or cp.light == 25:
        light = 1
    if cp.light == 24 or cp.light ==  23 or cp.light == 22:
        light = 2
    if cp.light == 21 or cp.light ==  20 or cp.light == 19:
        light = 3
    if cp.light == 18 or cp.light ==  17 or cp.light == 16:
        light = 4
    if cp.light == 15 or cp.light ==  14 or cp.light == 13:
        light = 5
    if cp.light == 12 or cp.light ==  11 or cp.light == 10:
        light = 6
    if cp.light == 9 or cp.light ==  8 or cp.light == 7:
        light = 7
    if cp.light == 6 or cp.light ==  5 or cp.light == 4:
        light = 8
    if cp.light == 3 or cp.light ==  2 or cp.light == 1:
        light = 9
    for i in range(0, light):
        cp.pixels[i] = ((125, 0, 0))
    for i in range(9, 9-light,-1):
        cp.pixels[i] = ((0, 0, 0 ))