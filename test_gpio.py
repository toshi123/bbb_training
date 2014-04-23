#!/usr/bin/env python

import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_12",GPIO.OUT)
GPIO.setup("P9_12",GPIO.IN)

while True:
    try:
        if GPIO.input("P9_12"):
            GPIO.output("P8_12",GPIO.LOW)
        else:
            GPIO.output("P8_12",GPIO.HIGH)
    except KeyboardInterrupt:
        break
GPIO.cleanup()

