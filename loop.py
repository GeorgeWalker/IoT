# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
from machine import Pin
import gc

#import webrepl
#webrepl.start()
gc.collect()
