#
#   Makerspace IoT class
#   
#   Find and display WiFi Access Points
#   Tested with Micropython release v1.8.7 (Jan 8, 2017)
#     
 
import network

#
#   create an interface that can connnect to a WIFI network
#
wifi = network.WLAN(network.STA_IF)

#
#   activate the WIFI interface
#
wifi.active(True)

#
# scan the WiFi network for Access Points (APs)
#
wifiAps = wifi.scan()

#
# print the APs that were found
#
if not wifiAps:
    print ("No Wifi Access Points were found")
else:
    for wifiAp in wifiAps:
        print (wifiAp)



  


