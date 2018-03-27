#18,23,24 are described as click, cancel, yes as  input pins
x=[18,23,24]
import RPi.GPIO as GPIO 
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(x[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(x[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(x[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if (GPIO.input(x[0])):
    sleep(0.1)
    if (GPIO.input(x[0])):
        click=GPIO.input(x[0])

if (GPIO.input(x[1])):
    sleep(0.1)
    if (GPIO.input(x[1])):
        cancel=GPIO.input(x[1])

if (GPIO.input(x[2])):
    sleep(0.1)
    if (GPIO.input(x[2])):
        yes=GPIO.input(x[2])
GPIO.cleanup() 
