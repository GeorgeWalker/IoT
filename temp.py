
import machine


def convertMCP9808ToDegC(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp

#
#   configure ESP8266 for I2C communication
#   GPIO4 pin is set to I2C SDA (data) 
#   GPIO5 pin is set to I2C SCL (clock) 
#
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))

#
# scan the I2C bus for attached sensors
#
i2cSensors = i2c.scan()

#
# print the I2C addresses of all sensors that were found
#
if not i2cSensors:
    print ("No I2C sensors were found")
else:
    print ("\nI2C sensor(s) found  !")
    for sensor in i2cSensors:
        print ("Sensor found with address = {}".format(sensor))

i2cDeviceAddress = 24
i2cRegisterAddress = 5
i2cNumBytesToRead = 2  

dataFromMCP9808 = i2c.readfrom_mem(i2cDeviceAddress, i2cRegisterAddress, i2cNumBytesToRead) 
tempInDegC = convertMCP9808ToDegC(dataFromMCP9808)

print(tempInDegC)

print ("done")
