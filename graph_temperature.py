from sense_hat import SenseHat

sense = SenseHat()

nothing = (0, 0, 0)
red = (255, 0, 0)

try:
    while True:
        temperature = sense.get_temperature()
        # print("Current Temperature: " + str(temperature))
        pixels = [red if i < temperature else nothing for i in range(64)]
        sense.set_pixels(pixels)
except KeyboardInterrupt:
    sense.clear()
    