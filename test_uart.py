#!/usr/bin/env python

import Adafruit_BBIO.UART as UART
import serial

UART.setup("UART1")
s = serial.Serial(port='/dev/ttyO1',baudrate=9600)
if s.isOpen():
    print 'serial port is open!'
    s.write("Hello World!")
s.close()
