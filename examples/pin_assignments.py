#!/usr/bin/python3
#
# pin_assignments.py
#
# Demonstration of how to use
# Raspberry Pi GPIO capabilities
# to control the lights on the LED 
# Jukebox.
#
# Peter F. Klemperer
# January 13, 2018

from gpiozero import Button, LED

# setup pins
# All Pin Numbers are Broadcom PIN
# See https://pinout.xyz for GPIO
# (pin header ordering) conversion
power_button_pin = 17
power_led_pin = 18

selection_1_button_pin = 22
selection_1_led_pin = 23

selection_2_button_pin = 9
selection_2_led_pin = 25

selection_2_button_pin = 9
selection_2_led_pin = 25

selection_3_button_pin = 11
selection_3_led_pin = 8

selection_4_button_pin = 0
selection_4_led_pin = 1

selection_5_button_pin = 6
selection_5_led_pin = 12

selection_6_button_pin = 19
selection_6_led_pin = 16

selection_7_button_pin = 26
selection_7_led_pin = 20

selection_8_button_pin = 27
selection_8_led_pin = 10

