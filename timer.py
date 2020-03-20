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
BLYNK_AUTH= "zUKQOvF40FkXYUg6VCh2uQd7N3gZZCxA"
blynk = blynklib.Blynk(BLYNK_AUTH)


# Error Message
WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_WRITE] Pin V{} Value: '{}' "
READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"

# Setup I2C for Accelerometer
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_mma8451.MMA8451(i2c) 

timer = blynktimer.Timer()

button_state = 0

def start_timer(vpin_num=0):
    start = time.perf_counter()
    return start

start_time = start_timer(0)

# Write time elapsed value to app based on button 
@blynk.handle_event('write V1')
def read_button(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global button_state
    button_state = int(value[0])
    #print(button_state)

@blynk.handle_event('write V2')
def read_image(pin, value):
	if button_state == 1:
		blynk.virtual_write(2, 1) # training in progress image
    elif button_state == 0: 
    	blynk.virtual_write(2, 2) # workout image

@timer.register(vpin_num=0, interval=1, run_once= False)
def elapsed_timer(vpin_num=0):
    #start_time = start_timer(0)
    #print(button_state)
    global start_time

    if button_state == 1:
        seconds = round(time.perf_counter() - start_time)
        m,s = divmod(seconds, 60)
        h,m = divmod(m, 60)
        time.sleep(1)
        elapsed_time = '{:d}:{:02d}:{:02d}'.format(h,m,s)
        
        print(WRITE_EVENT_PRINT_MSG.format(0, elapsed_time))
        blynk.virtual_write(0, elapsed_time)
    elif button_state == 0:
        #print('blah')
        start_time = start_timer(0)

while True:
    blynk.run()
    timer.run()
