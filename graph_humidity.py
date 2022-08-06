from sense_hat import SenseHat

sense = SenseHat()

nothing = (0, 0, 0)
cyan = (0, 255, 255)

try:
    while True:
        humidity = sense.get_humidity()
        humidity_value = 64 * humidity / 100
        # print("Current Humidity: " + str(humidity))
        pixels = [cyan if i < humidity_value else nothing for i in range(64)]
        sense.set_pixels(pixels)
except KeyboardInterrupt:
    sense.clear()
    