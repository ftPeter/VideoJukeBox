#!/usr/bin/env python3
from gpiozero import Button, LED
from signal import pause
import os, sys

from pin_assignments import *

def when_pressed():
    # start blinking with 1/2 second rate
    led.blink(on_time=0.5, off_time=0.5)
    print("SHUTDOWN PRESSED")

def when_released():
    # be sure to turn the LEDs off if we release early
    led.on()
    print("SHUTDOWN CANCLED")

def shutdown():
    print("SIMULATED SHUTDOWN")
    #os.system("sudo poweroff")

holdTime = 15

led = LED(power_led_pin)
btn = Button(power_button_pin, hold_time=holdTime)
btn.when_held = shutdown
btn.when_pressed = when_pressed
btn.when_released = when_released
pause()

