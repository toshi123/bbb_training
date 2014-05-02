#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
from Adafruit_I2C import Adafruit_I2C

def initI2C(i2c):
    i2c.write8(0,0x38)
    i2c.write8(0,0x39)
    i2c.write8(0,0x14)
    i2c.write8(0,0x70)
    i2c.write8(0,0x56)
    i2c.write8(0,0x6c)
    i2c.write8(0,0x38)
    i2c.write8(0,0x0d)
    i2c.write8(0,0x01)

def writeMessage(i2c,message,position=0,timeofspan="        "):
    if sleeptime != "        ":
        sleeptime = " "+str(timeofspan)[0:5]+"sec"

    i2c.write8(0,0x01) # initialize LCD
    for p in timeofspan:
        i2c.write8(0x40,ord(p))
    i2c.write8(0,0xc0) # new line
    for p in range(position,position+8):
        q = p
        if p >= len(message):
            q = p%len(message)
        i2c.write8(0x40,ord(message[q]))
    position += 1
    return position

GPIO.setup("P9_12", GPIO.IN)
GPIO.setup("P8_12", GPIO.OUT)
ADC.setup()
PWM.start("P9_14", 0)

isUp = False
isInit = False
duty = 100
span = 5
p = 0
pasttime = 0
while True:
    try:
        # Switch ON
        if not GPIO.input("P9_12"):
            # LED
            if isUp:
                duty += span
            if duty >= 100:
                    duty = 100
                    isUp = False
            else:
                duty -= span
                if duty <= 5:
                    duty = 5 
                    isUp = True
            PWM.set_duty_cycle("P9_14", duty)

            # LCD
            GPIO.output("P8_12", GPIO.HIGH)
            # initi2c LCD
            if not isInit:
                time.sleep(0.1)
                i2c = Adafruit_I2C(0x3e)
                initI2C(i2c)
                isInit = True
            if pasttime > 0.3:
                p = writeMessage(\
                    i2c,\
                    "PowerOn! ",\
                    position = p,\
                    sleeptime = sleeptime*40\
                )
                pasttime = 0

        # Switch OFF
        else:
            # LED
            duty -= span
            if duty < 0:
                duty = 0
            PWM.set_duty_cycle("P9_14",duty)

            #LCD
            if isInit and duty == 0:
                writeMessage(i2c,"bye..   ")
                time.sleep(0.5)
                GPIO.output("P8_12", GPIO.LOW)
                isInit = False

        sleeptime = ADC.read("P9_39") * 0.5
        time.sleep(sleeptime)
        pasttime += sleeptime
    except KeyboardInterrupt:
        break

PWM.stop("P9_14")
PWM.cleanup()

