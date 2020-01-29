import sensor,image,time
from modules import ws2812
from Maix import GPIO
from fpioa_manager import fm
#import lcd

print("start")

class_ws2812 = ws2812(8, 1)

a = class_ws2812.set_led(0, (255, 0, 255))
a = class_ws2812.display()

fm.register(18, fm.fpioa.GPIO1, force=True)
fm.register(19, fm.fpioa.GPIO2, force=True)
button_a = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
button_b = GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)

#lcd.init(freq=15000000)
#lcd.rotation(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_vflip(1)
sensor.run(1)

try:
    while(True):
        img = sensor.snapshot()
        print(button_a.value())
        print(button_b.value())
        if (button_a.value() == 0):
            a = class_ws2812.set_led(0, (0, 255, 0))
            a = class_ws2812.display()
        elif (button_b.value() == 0):
            a = class_ws2812.set_led(0, (0, 0, 255))
            a = class_ws2812.display()
        else:
            a = class_ws2812.set_led(0, (255, 0, 0))
            a = class_ws2812.display()


        time.sleep(1);
except Exception as e:
    print("exception")

finally:
    print("finally")

print("finish")

