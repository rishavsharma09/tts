
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
currstate=0
prevstate=0
y=0
x=0
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
while(1):
    currstate=GPIO.input(18)
    if (currstate!=prevstate):
        if (currstate == 1):
            x=1
    else: 
        x=0
    time.sleep(0.1)
    prevstate=currstate
    while (x == 1):
        print ("t")
        print ("p")
        x=0



