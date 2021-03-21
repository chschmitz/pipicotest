from machine import Pin, PWM
from utime import sleep

analog_value = machine.ADC(26)
led = Pin(25, Pin.OUT)

minsleep = 0.05
maxsleep = 1.0

while True:
    freq = analog_value.read_u16()
    slp = minsleep + (maxsleep - minsleep) * freq / 65535.0
    print(slp)
    led.toggle()
    sleep(slp)