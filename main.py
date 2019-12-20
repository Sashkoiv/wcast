from machine import Pin, I2C
from time import sleep
import display
from sinoptik import Sinoptik


i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
oled = display.SSD1306_I2C(128, 64, i2c)

weather = Sinoptik()
data = weather.forecast

oled.fill(0)
oled.text(data[1][0], 0, 0)
oled.text(data[1][1], 0, 10)
oled.text(data[1][2], 0, 20)
oled.text('{} Celsius'.format(data[1][3]), 0, 30)
oled.text('{} Celsius'.format(data[1][4]), 0, 40)

oled.show()