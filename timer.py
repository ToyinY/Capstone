## Writes values to app.
## Pins must be on Push setting

import busio
import adafruit_mma8451 
import time
import blynktimer
import random
import blynklib
import board

# Set up Blynk
BLYNK_AUTH= "n3rlQoz_veIonWxZG-rfLqQoUh75BnQW"
blynk = blynklib.Blynk(BLYNK_AUTH)


#Error Message
WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_WRITE] Pin V{} Value: '{}' "

#Setup I2C for Accelerometer
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_mma8451.MMA8451(i2c) 

timer = blynktimer.Timer()


# Write accelerometer values to app 
@timer.register(vpin_num=22, interval=1, run_once= False)
@timer.register(vpin_num=23, interval=1, run_once= False)
@timer.register(vpin_num=24, interval=1, run_once= False)
@timer.register(vpin_num=25, interval=1, run_once= False)
def write_acc_to_virtual_pin(vpin_num=1):
    x, y, z, orientation = read_acc()
    if vpin_num == 22:
        print(WRITE_EVENT_PRINT_MSG.format(vpin_num, x))
        blynk.virtual_write(vpin_num, x)
    if vpin_num == 23:
        print(WRITE_EVENT_PRINT_MSG.format(vpin_num, y))
        blynk.virtual_write(vpin_num, y)
    if vpin_num == 24:
        print(WRITE_EVENT_PRINT_MSG.format(vpin_num, z))
        blynk.virtual_write(vpin_num, z)
    if vpin_num == 25:
        print(WRITE_EVENT_PRINT_MSG.format(vpin_num, orientation))
        blynk.virtual_write(vpin_num, orientation)

# Read accelerometer values 
def read_acc():
    x,y,z = sensor.acceleration
    #print(READ_PRINT_MSG.format(pin))
    orientation = sensor.orientation 
    #time.sleep(1)
    return x, y, z, orientation

while True:
    blynk.run()
    timer.run() 
