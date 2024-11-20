from adafruit_circuitplayground import cp

while True:
        if cp.switch:
            for i in range(0,5):
                cp.pixels[i] = ((0, 255, 0))
        else:
            for i in range(5,10):
                cp.pixels[i] = ((0, 255, 0))
        if cp.switch:
             for j in range(5,10):
                  cp.pixels[j] = (0, 0, 0)
        else:
             for j in range(0,5):
                  cp.pixels[j] = (0, 0, 0)