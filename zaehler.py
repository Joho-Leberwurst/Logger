from RPi import GPIO
from time import *
import os
GPIO.setmode(GPIO.BOARD)


counter = 0

impulsbreite = 65 # (millisec)
toleranz     =  20 # (millisec)
pin     = 5
#UUID = 775e6cb0-78c2-11e4-9094-bd95e29b6ac6

GPIO.setup(pin, GPIO.IN)
t_start = 0

while True:
    if (GPIO.input(pin) < 1):
        if (t_start == 0):
            t_start = time()
        if ( time() - t_start ) >= ( (impulsbreite-toleranz)/1000 ):
            os.system("wget -O /dev/null http://localhost/middleware.php/data/e0266bf0-d009-11e4-b77e-f343d3e237a3.json?operation=add&value=1")
            counter += 1
            print(counter)
            t_start = 0
            sleep(0.1)
    else:
        t_start = 0