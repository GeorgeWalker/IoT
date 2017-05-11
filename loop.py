# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
from machine import Pin
import gcimport utime

#import webrepl
#webrepl.start()
gc.collect()led = Pin(16, Pin.OUT) # red ledfor counter in range(1,200):    led.value(0)    utime.sleep_ms(200)    led.value(1)    utime.sleep_ms(200)

