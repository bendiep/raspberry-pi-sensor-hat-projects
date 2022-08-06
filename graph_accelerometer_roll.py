from sense_hat import SenseHat

sense = SenseHat()

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
cyan = (0, 255, 255)

try:
    while True:
        accelerometer_data = sense.get_accelerometer()
        roll_value = accelerometer_data["roll"]
        # print("Current Roll: " + str(roll_value))

        pixels = []
        for i in range(64):
            if (roll_value >= 0 and roll_value <= 90):
                if (i <= 31):
                    pixels.append(green)
                else:
                    if (i / 32 < roll_value / 16):
                        pixels.append(green)
                    else:
                        pixels.append(white)
            elif (roll_value <= 360 and roll_value >= 270):
                if (i >= 32):
                    pixels.append(white)
                else:
                    if (i / 32 < (roll_value - 270) / 96):
                        pixels.append(green)
                    else:
                        pixels.append(white)
            else:
                pixels.append(red)
        sense.set_pixels(pixels)
except KeyboardInterrupt:
    sense.clear()
 