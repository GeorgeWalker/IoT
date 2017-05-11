#
#   Makerspace IoT class
#   
#   Connect to WIFI
#   Tested with Micropython release v1.8.7 (Jan 8, 2017)
#     
 
import network

#
#   WIFI connection information
#   
#   replace WIFI-SSID and WIFI-PASSWORD with access information for the WIFI network you will connect to
#

wifiSSID = "iotclass" 
wifiPassword = "iotclass" 

#
#   create an interface that can connnect to a WIFI network
#
wifi = network.WLAN(network.STA_IF)

#
#   activate the WIFI interface
#
wifi.active(True)

#
#   connect the ESP8266 device to the WIFI network
#
wifi.connect(wifiSSID, wifiPassword)

#
#   wait until the ESP8266 has successfully connected to the WIFI network
# 
while not wifi.isconnected():
  pass
  
#
#   if we made it here, WooHoo, we've got WIFI access !
#
print('\nLife is GREAT !   We have WIFI access\n')

#
#   see what Internet access information was received (e.g. IP Address)
#
print('Network access information: \n', wifi.ifconfig())

  


