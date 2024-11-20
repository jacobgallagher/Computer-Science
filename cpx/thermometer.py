from adafruit_circuitplayground import cp
import time


cp.pixels.brightness = 0.02

while True:
    temp_f = cp.temperature
    temp = (temp_f * 9 / 5) + 32 
    if temp < 60:
        cp.pixels[0] = (0, 0, 255)

    if temp > 60:
        cp.pixels[1] = (28, 0, 227)

    if temp > 64:
        cp.pixels[2] = (57, 0, 199)

    if temp > 68:
        cp.pixels[3] = (85, 0, 170)

    if temp > 72:
        cp.pixels[4] = (113, 0, 142)

    if temp > 76:
        cp.pixels[5] = (142, 0, 113)

    if temp > 80:
        cp.pixels[6] = (170, 0, 85)
    
    if temp > 84:
        cp.pixels[7] = (199, 0, 57)
    
    if temp > 88:
        cp.pixels[8] = (227, 0, 28)

    if temp > 92:
        cp.pixels[9] = (255, 0, 0)
    time.sleep(.5)