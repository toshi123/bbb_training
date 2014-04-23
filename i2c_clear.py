import time
from Adafruit_I2C import Adafruit_I2C

i2c = Adafruit_I2C(0x3e)
i2c.write8(0,0x38)
i2c.write8(0,0x39)
i2c.write8(0,0x14)
i2c.write8(0,0x70)
i2c.write8(0,0x56)
i2c.write8(0,0x6c)
i2c.write8(0,0x38)
i2c.write8(0,0x0d)
i2c.write8(0,0x01)
time.sleep(0.2)

for c in "        ":
    i2c.write8(0x40,ord(c))

i2c.write8(0,0xc0)
for c in "        ":
    i2c.write8(0x40,ord(c))
