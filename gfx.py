import machine
import ssd1306
import utime
import framebuf
from math import ceil

width = 128
height = 64

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000) 
print(i2c.scan())

display = ssd1306.SSD1306_I2C(width, height, i2c)
fbuf = framebuf.FrameBuffer(bytearray(ceil(width * height / 8)), width, height, framebuf.MONO_HMSB)

x = 0
y = 10
dx = 2 
dy = 3

txt = "Bang!"
txtx = len(txt) * 8
txty = 8
limx = width - txtx
limy = height - txty

while True:
    fbuf.fill(0)
    fbuf.text(txt, x, y, 1)
    display.blit(fbuf, 0, 0)
    display.show()
    x += dx
    y += dy
    if (x > limx) or (x < 1): dx *= -1
    if (y > limy) or (y < 1): dy *= -1
    