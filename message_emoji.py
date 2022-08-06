from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(180)
sense.low_light = True

nothing = (0, 0, 0)
white = (255, 255, 255)
pink = (255, 105, 180)

def heart():
    P = pink
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, P, P, O, P, P, O, O,
        P, P, P, P, P, P, P, O,
        P, P, P, P, P, P, P, O,
        O, P, P, P, P, P, O, O,
        O, O, P, P, P, O, O, O,
        O, O, O, P, O, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo

def letter_i():
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo

def letter_d():
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, W, W, W, O, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, W, O, W, W, O,
        O, O, W, W, O, W, W, O,
        O, O, W, W, W, W, O, O,
        O, O, W, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo

def char_period():
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, W, W, W, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo

images = [letter_i, heart, letter_d, char_period]
count = 0

try:
    while True:
        sense.set_pixels(images[count % len(images)]())
        time.sleep(.75)
        count += 1
except KeyboardInterrupt:
    sense.clear()
