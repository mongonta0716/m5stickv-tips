import lcd
import utime
import sys
import pmu
from machine import I2C
from Maix import GPIO
from fpioa_manager import *

axp = pmu.axp192()

axp.enableADCs(True)

lcd.init()
lcd.draw_string(0, 0, "Battery Info SD boot.py", lcd.WHITE, lcd.BLACK)
lcd.draw_string(230, 0, "*", lcd.BLUE, lcd.BLACK)

try:
  while(True):
    val = axp.getVbatVoltage()
    lcd.draw_string(0, 15, "Battery Voltage:" + str(val), lcd.RED, lcd.BLACK)

    val = axp.getUSBVoltage()
    lcd.draw_string(0, 30, "USB Voltage:" + str(val), lcd.WHITE, lcd.BLACK)

    val = axp.getUSBInputCurrent()
    lcd.draw_string(0, 45, "USB InputCurrent:" + str(val), lcd.RED, lcd.BLACK)

    val = axp.getBatteryDischargeCurrent()
    lcd.draw_string(0, 60, "DischargeCurrent:" + str(val), lcd.GREEN, lcd.BLACK)

    val = axp.getBatteryInstantWatts()
    lcd.draw_string(0, 75, "Instant Watts:" + str(val), lcd.BLUE, lcd.BLACK)

    val = axp.getTemperature()
    lcd.draw_string(0, 90, "Temperature:" + str(val), lcd.BLUE, lcd.BLACK)

    utime.sleep(1)

except KeyboardInterrupt:
  lcd.draw_string(230, 0, " ", lcd.BLUE, lcd.BLACK)
  sys.exit()