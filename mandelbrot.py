import machine
import ssd1306
import utime
import framebuf
from math import ceil
 
def scale(from_min, from_max, to_min, to_max, value):
    return to_min + ((value - from_min) / (from_max - from_min)) * (to_max - to_min)   
           
           
MAXITER = 100
def mandel_iter(x, y):
    (cr, ci) = (x, y)
    (zr, zi) = (0, 0)
    
    i = 0
    (zrs, zis) = (zr*zr, zi*zi)
    while (i < MAXITER) and (zrs + zis < 4):
        (zr, zi) = (zrs - zis + cr, zr * zi)
        zi += zi + ci
        i += 1
        (zrs, zis) = (zr*zr, zi*zi)
        
    return 0 if i < MAXITER else 1
          
width = 128
height = 64

x0 = -2.2
x1 = 1.4
y0 = -1
y1 = 1

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000) 
print(i2c.scan())

display = ssd1306.SSD1306_I2C(width, height, i2c)
fbuf = framebuf.FrameBuffer(bytearray(ceil(width * height / 8)), width, height, framebuf.MONO_HMSB)

fbuf.fill(0)
for yp in range(height):
    for xp in range(width):
        (x, y) = (scale(0, width, x0, x1, xp), scale(0, height, y0, y1, yp))
        color = mandel_iter(x, y)
        display.pixel(xp, yp, color)
    print(yp)
    display.show()
        
#display.blit(fbuf, 0, 0)
#display.show()
  