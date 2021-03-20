import machine
import ssd1306
import utime

value = 0


sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000) 
print(i2c.scan())

display = ssd1306.SSD1306_I2C(128, 64, i2c)

def disp():
    global display
    display.fill(0)
    display.text("Wert ist: %d" % value, 20, 20, 1)
    display.fill_rect(0, 40, value, 5, 1)
    display.show()
    
def decrement(pin):
    global value
    value -= 1
    if (value < 0): value = 0
    disp()

def increment(pin):
    global value
    value += 1
    if value > 123: value = 123
    disp()

gp5 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
gp5.irq(increment, machine.Pin.IRQ_FALLING)

gp6 = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
gp6.irq(decrement, machine.Pin.IRQ_FALLING)