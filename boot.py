
C:\dev\IoT>call ampy -pCOM3 get boot.py 
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
#import webrepl
#webrepl.start()
gc.collect()

