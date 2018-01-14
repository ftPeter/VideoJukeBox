#!/usr/bin/python3
#
# button_light_io.py
#
# Demonstration of how to use
# Raspberry Pi GPIO capabilities
# to control the lights on the LED 
# Jukebox.
#
# Peter F. Klemperer
# January 13, 2018

from gpiozero import Button, LED

from signal import pause

power_button = Button(17)
power_led    = LED(18)

power_button.when_pressed  = power_led.on
power_button.when_released = power_led.off

pause()
