import machine
import ssd1306

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000) 
print(i2c.scan())

display = ssd1306.SSD1306_I2C(128, 64, i2c)
temp_sensor = machine.ADC(4)

def get_temp():
    global temp_sensor 
    temp = temp_sensor.read_u16()
    temperature_volts = temp * 3.3 / 65535
    celsius = 27 - (temperature_volts - 0.706) / 0.001721
    return celsius

dir = 2
x = 0
def show_temp():
    global display, dir, x
    display.fill(0)
   
    display.text("Temperatur", 20, 20, 1)
    display.text("%2.2f" % get_temp(), 20, 30, 1)
    
    display.rect(x, 45, 10, 5, 5)
    x = x + dir
    if (x > 122) or (x < 2):
        dir = -dir
       
    display.show()
    
def ping(timer):
       show_temp()
  
timer = machine.Timer()
timer.init(freq = 1.0/4.0, mode = machine.Timer.PERIODIC, callback = ping)
show_temp()