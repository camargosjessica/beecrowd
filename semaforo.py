import time


class ColorLight:
    color = str
    color_time = int

    def __init__(self, color, color_time):
        self.color = color
        self.color_time = color_time


green = ColorLight("Green", 5)
yellow = ColorLight("Yellow", 2)
red = ColorLight("Red", 7)

lights = [green, yellow, red]

while True:
    for light in lights:
        print(light.color)
        time.sleep(light.color_time)
