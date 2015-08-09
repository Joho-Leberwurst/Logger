from RPi import GPIO
from time import *
import os
GPIO.setmode(GPIO.BOARD)


counter1 = 0
counter2 = 0
counter3 = 0

impulsbreite = 65 # (millisec)
toleranz     =  20 # (millisec)
pin1  = 7
uuid1 = "3859fde0-2ab5-11e5-8127-0df9ef013463"

pin2  = 11
uuid2 = "fc35a860-3e9d-11e5-a05a-7786d0ce58f9"

pin3  = 13
uuid3 = "1d083960-3e9e-11e5-ab65-c39324b86969"

# uuid4 = "53cf1e00-3ec1-11e5-a9cf-45d18ce862ae"  # Kummulierter Kanal (1+2+3)

GPIO.setup(pin1, GPIO.IN)
GPIO.setup(pin2, GPIO.IN)
GPIO.setup(pin3, GPIO.IN)

t_start1 = 0
went_through_zero1 = True

t_start2 = 0
went_through_zero2 = True

t_start3 = 0
went_through_zero3 = True

while True:
    if (GPIO.input(pin1) < 1):
        if (went_through_zero1):
            if (t_start1 == 0):
                t_start1 = time()
            if ( time() - t_start1 ) >= ( (impulsbreite-toleranz)/1000 ):
                os.system("wget -O /dev/null http://localhost/middleware.php/data/" + uuid1 + ".json?operation=add&value=1 --nv &")
                counter1 += 1
                print(counter1)
                t_start1 = 0
                went_through_zero1 = False
                sleep(0.1)
    else:
        t_start1 = 0
        went_through_zero1 = True
    
    if (GPIO.input(pin2) < 1):
        if (went_through_zero2):
            if (t_start2 == 0):
                t_start2 = time()
            if ( time() - t_start2 ) >= ( (impulsbreite-toleranz)/1000 ):
                os.system("wget -O /dev/null http://localhost/middleware.php/data/" + uuid2 + ".json?operation=add&value=1 --nv &")
                counter2 += 1
                print(counter2)
                t_start2 = 0
                went_through_zero2 = False
                sleep(0.1)
    else:
        t_start2 = 0
        went_through_zero2 = True
        
    if (GPIO.input(pin3) < 1):
        if (went_through_zero3):
            if (t_start3 == 0):
                t_start3 = time()
            if ( time() - t_start3 ) >= ( (impulsbreite-toleranz)/1000 ):
                os.system("wget -O /dev/null http://localhost/middleware.php/data/" + uuid3 + ".json?operation=add&value=1 --nv &")
                counter3 += 1
                print(counter3)
                t_start3 = 0
                went_through_zero3 = False
                sleep(0.1)
    else:
        t_start3 = 0
        went_through_zero3 = True
