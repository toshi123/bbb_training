import time
from Adafruit_BBIO.SPI import SPI

spi_in = SPI(0,0)
spi_out = SPI(0,1)

while True:
    try:
        spi_out.writebytes([0x50])
        print spi_in.readbytes(2)
        time.sleep(0.02)
    except KeyboardInterrupt:
        break

