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

# setup pins
# All Pin Numbers are Broadcom PIN
# See https://pinout.xyz for GPIO
# (pin header ordering) conversion
power_button = Button(17)
power_led    = LED(18)

selection_1_button = Button(22)
selection_1_led    = LED(23)

selection_2_button = Button(9)
selection_2_led    = LED(25)

selection_3_button = Button(11)
selection_3_led    = LED(8)

selection_4_button = Button(0)
selection_4_led    = LED(1)

selection_5_button = Button(6)
selection_5_led    = LED(12)

selection_6_button = Button(19)
selection_6_led    = LED(16)

selection_7_button = Button(26)
selection_7_led    = LED(20)

selection_8_button = Button(27)
selection_8_led    = LED(10)
# setup complete

# main'ish:
power_led.source = power_button.values
selection_1_led.source = selection_1_button.values
selection_2_led.source = selection_2_button.values
selection_3_led.source = selection_3_button.values
selection_4_led.source = selection_4_button.values
selection_5_led.source = selection_5_button.values
selection_6_led.source = selection_6_button.values
selection_7_led.source = selection_7_button.values
selection_8_led.source = selection_8_button.values

pause()
