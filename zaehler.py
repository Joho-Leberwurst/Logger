from RPi import GPIO
from time import *
import os


#set GPI Mode
GPIO.setmode(GPIO.BCM)

phaseOne     = 13
uuid = "1d083960-3e9e-11e5-ab65-c39324b86969"

def inter( ):
    try:  
        GPIO.wait_for_edge(phaseOne, GPIO.RISING)  
        print "Signal"
        os.system("wget -O /dev/null http://localhost/middleware.php/data/" + uuid + ".json?operation=add&value=1 --nv &") 
        inter( )
    except KeyboardInterrupt:  
        GPIO.cleanup( )  


# set pin to pull_up_down
GPIO.setup(phaseOne, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
try:  
    GPIO.wait_for_edge(phaseOne, GPIO.RISING)  
    os.system("wget -O /dev/null http://localhost/middleware.php/data/" + uuid + ".json?operation=add&value=1 --nv &") 
    inter( )
except KeyboardInterrupt:  
    GPIO.cleanup( )  
    
