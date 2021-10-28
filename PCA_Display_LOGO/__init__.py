import gc

import defines, rgb, buttons, system
from time import sleep

UP, DOWN, LEFT, RIGHT = defines.BTN_UP, defines.BTN_DOWN, defines.BTN_LEFT, defines.BTN_RIGHT
direction = ''
B = (0, 0, 0)
W = (255, 255, 255)
Y = (255, 128, 0)

PCA = [
    [Y, Y, Y, Y, Y, B, B, B, B, B, B, B, B, W, W, W, W, W, B, B, B, B, B, B, B, B, B, B, B, Y, Y, Y],
    [Y, Y, Y, Y, B, B, B, B, B, B, B, B, B, W, W, B, B, W, W, B, B, B, B, B, B, B, B, B, Y, Y, Y, Y],
    [Y, Y, B, B, B, B, B, B, B, B, B, B, B, W, W, B, B, W, W, B, B, B, B, B, B, B, B, B, B, B, Y, Y],
    [Y, Y, B, B, B, B, B, B, B, B, B, B, B, W, W, B, B, W, W, B, B, B, B, B, B, B, B, B, B, B, Y, Y],
    [Y, Y, B, B, B, B, B, B, B, B, B, B, B, W, W, B, B, W, B, B, B, B, B, B, B, B, B, B, B, B, Y, Y],
    [Y, Y, B, B, B, B, B, B, B, B, B, B, B, W, W, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, Y, Y],
    [Y, Y, Y, Y, B, B, B, B, B, B, B, B, B, W, W, W, B, B, B, B, B, B, B, B, B, B, B, B, Y, Y, Y, Y],
    [Y, Y, Y, Y, B, B, B, B, B, B, B, B, B, W, W, W, B, B, B, B, B, B, B, B, B, B, B, B, Y, Y, Y, Y]
]


def input_B(pressed):
    global direction
    print("Exiting")
    direction = defines.BTN_B


buttons.register(defines.BTN_B, input_B)

rgb.background()
rgb.setbrightness(3)
gc.collect()

while direction != defines.BTN_B:
    gc.collect()
    rgb.disablecomp()
    rgb.clear()
    for row_id, row in enumerate(PCA, 0):
        for col_id, pixel in enumerate(row, 0):
            rgb.pixel(pixel, (col_id, row_id))

    rgb.enablecomp()
    sleep(0.05)
    rgb.clear()
    sleep(0.05)

system.reboot()