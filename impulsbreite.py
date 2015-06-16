from RPi import GPIO
from time import *
import os
GPIO.setmode(GPIO.BOARD)

pin     = 5
GPIO.setup(pin, GPIO.IN)
t_start = 0
t_stop = 0

while True:
    if (GPIO.input(pin) < 1):
        if (t_start == 0):
            t_start = time()
    else:
        delta = time() - t_start
        if (t_start > 0):
            print(delta)
	    	lt = localtime()
	    	now = strftime("%d.%m.%Y %H:%M:%S", lt)
	    	text_file = open("impulsbreiten.txt", "a")
	    	text_file.write(now + ";" + `delta` + "\n")
	    	text_file.close()
        t_start = 0