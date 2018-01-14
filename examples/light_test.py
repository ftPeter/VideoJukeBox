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

from time import sleep

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
sleep_delay_s = 0.5
while(True):
    power_led.on()
    sleep(sleep_delay_s)
    power_led.off()

    selection_1_led.on()
    sleep(sleep_delay_s)
    selection_1_led.off()

    selection_2_led.on()
    sleep(sleep_delay_s)
    selection_2_led.off()

    selection_3_led.on()
    sleep(sleep_delay_s)
    selection_3_led.off()

    selection_4_led.on()
    sleep(sleep_delay_s)
    selection_4_led.off()

    selection_5_led.on()
    sleep(sleep_delay_s)
    selection_5_led.off()

    selection_6_led.on()
    sleep(sleep_delay_s)
    selection_6_led.off()

    selection_7_led.on()
    sleep(sleep_delay_s)
    selection_7_led.off()

    selection_8_led.on()
    sleep(sleep_delay_s)
    selection_8_led.off()

