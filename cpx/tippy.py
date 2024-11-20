
while True:
    x = cp.acceleration.x

    if x < -2:
        cp.pixels[1] = (0, 0, 0)
        cp.pixels[2] = (0, 0, 0)
        cp.pixels[3] = (0, 0, 0)

        cp.pixels[6] = (255, 0, 0)
        cp.pixels[7] = (255, 0, 0)
        cp.pixels[8] = (255, 0, 0)

    elif x > 2:
        cp.pixels[1] = (0, 255, 0)
        cp.pixels[2] = (0, 255, 0)
        cp.pixels[3] = (0, 255, 0)

        cp.pixels[6] = (0, 0, 0)
        cp.pixels[7] = (0, 0, 0)
        cp.pixels[8] = (0, 0, 0)
        
        

    else:
        cp.pixels[1] = (0, 0, 0)
        cp.pixels[2] = (0, 0, 0)
        cp.pixels[3] = (0, 0, 0)
        cp.pixels[6] = (0, 0, 0)
        cp.pixels[7] = (0, 0, 0)
        cp.pixels[8] = (0, 0, 0)

    
    

