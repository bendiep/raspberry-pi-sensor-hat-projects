from sense_hat import SenseHat

sense = SenseHat()

nothing = (0, 0, 0)
blue = (0, 0, 255)

try:
    while True:
        pressure = sense.get_pressure()
        pressure_value = (64 * pressure) / 1260
        # print("Current Pressure: " + str(pressure))
        pixels = [blue if i < pressure_value else nothing for i in range(64)]
        sense.set_pixels(pixels)
except KeyboardInterrupt:
    sense.clear()
