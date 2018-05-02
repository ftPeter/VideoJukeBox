# python-keyboard
#
# example of linking raspberry pi GPIOzero 
# to the py-uinput library

import uinput

device = uinput.Device([
    uinput.KEY_1,
    uinput.KEY_2,
    uinput.KEY_3,
    uinput.KEY_4,
    uinput.KEY_5,
    uinput.KEY_R,
    uinput.KEY_S,
    ])

device.emit_click(uinput.KEY_1)
device.emit_click(uinput.KEY_R)

