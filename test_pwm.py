#!/usr/bin/env python

import time
import Adafruit_BBIO.PWM as PWM

PWM.start("P9_22",5,50)

while True:
    try:
        duty = float(raw_input("Input duty ratio: "))
        if duty < 0.0:
            duty = 0.0
        elif duty > 100.0:
            duty = 100.0
        print duty
        PWM.set_duty_cycle("P9_22",duty)
        time.sleep(0.02)
    except KeyboardInterrupt:
        break
PWM.stop("P9_22")
PWM.cleanup()
