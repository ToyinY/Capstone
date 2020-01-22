# Write sensor values to app
# Virtual pins on app must be set to refresh every 1 second

import BlynkLib
import busio
import adafruit_mma8451
import board

blynk = BlynkLib.Blynk("n3rlQoz_veIonWxZG-rfLqQoUh75BnQW")
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_mma8451.MMA8451(i2c)


@blynk.VIRTUAL_READ(22)
def my_read_handler_x():
    x, _, _, _ = read_virtual_pin_handler()
    print(str(22))
    blynk.virtual_write(22, x) 

@blynk.VIRTUAL_READ(23)
def my_read_handler_y():
    _, y, _, _ = read_virtual_pin_handler()
    print(str(23))
    blynk.virtual_write(23, y)
    
@blynk.VIRTUAL_READ(24)
def my_read_handler_z():
    _, _, z, _ = read_virtual_pin_handler()
    print(str(24))
    blynk.virtual_write(24, z)

@blynk.VIRTUAL_READ(25)
def my_read_handler_orientation():
    _, _, _, orientation = read_virtual_pin_handler()
    print(str(25))
    blynk.virtual_write(25, orientation) 


def read_virtual_pin_handler():
    x,y,z = sensor.acceleration
    orientation = sensor.orientation 
    #time.sleep(1)
    return x, y, z, orientation


while True:
    blynk.run()

