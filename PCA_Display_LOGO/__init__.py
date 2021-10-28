import gc

import defines, display, buttons, system
from time import sleep

UP, DOWN, LEFT, RIGHT = defines.BTN_UP, defines.BTN_DOWN, defines.BTN_LEFT, defines.BTN_RIGHT
direction = ''
B = [0x000000]
W = [0xFFFFFF]
Y = [0xFF9900]

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
gc.collect()

while direction != defines.BTN_B:
    gc.collect()
    for row_id, row in enumerate(PCA, 0):
        for col_id, pixel in enumerate(row, 0):
            display.drawPixel(pixel, (col_id, row_id))

    display.flush()

system.reboot()