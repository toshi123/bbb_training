#!/usr/bin/env python

import time
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM

ADC.setup()
PWM.start("P9_14",0)

while True:
    try:
        duty = ADC.read("P9_39")*100
        PWM.set_duty_cycle("P9_14",duty)
        time.sleep(0.03)
    except KeyboardInterrupt:
        break
PWM.stop("P9_14")
PWM.cleanup()
