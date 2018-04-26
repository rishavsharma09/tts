from num2words import num2words
from subprocess import call
import RPi.GPIO as GPIO 
from time import sleep

speakfulltext():
    cmd_beg= 'espeak '
    cmd_end= '2>/dev/null'
    f=open("full.txt", "r")
    if f.mode == 'r':
        text =f.read()
    text = text.replace(' ', '_')
    call([cmd_beg+text+cmd_end], shell=True)
    return 1
displaytext():
    GPIO.setmode(GPIO.BCM)
    bit=[16,13,21,19,20,26]
    for i in range(0,6):
         GPIO.setup(bit[i], GPIO.OUT, initial=1)
    strring='abc'

    for ltt in strring:
       if ltt in ('a','A'):
            GPIO.output(bit[0],0)
            sleep(2)
            GPIO.output(bit[0],1)

        elif ltt in ('b','B'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[2],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[2],1)


        elif ltt in ('c','C'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[1],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[1],1)


        elif ltt in ('d', 'D'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[1],0)
            GPIO.output(bit[3],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[1],1)
            GPIO.output(bit[3],1)


        elif ltt in ('e', 'E'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[3],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[3],1)

        elif ltt in ('f', 'F'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[1],0)
            GPIO.output(bit[2],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[1],1)
            GPIO.output(bit[2],1)


        elif ltt in ('g','G'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[1],0)
            GPIO.output(bit[2],0)
            GPIO.output(bit[3],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[1],1)
            GPIO.output(bit[2],1)
            GPIO.output(bit[3],1)


        elif ltt in ('h','H'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[2],0)
            GPIO.output(bit[3],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[2],1)
            GPIO.output(bit[3],1)
 

        elif ltt in ('i','I'):
            GPIO.output(bit[1],0)
            GPIO.output(bit[2],0)
            sleep(2)
            GPIO.output(bit[1],1)
            GPIO.output(bit[2],1)

       elif ltt in 'j', 'J':
            GPIO.output(bit[1],0)
            GPIO.output(bit[2],0)
            GPIO.output(bit[3],0)
            sleep(2)
            GPIO.output(bit[1],1)
            GPIO.output(bit[2],1)
            GPIO.output(bit[3],1)


       elif ltt in ('k', 'K'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[4],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[4],1)


       elif ltt in ('l','L'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[2],0)
            GPIO.output(bit[4],0)
            sleep(2)
            GPIO.output(bit[0],0)
            GPIO.output(bit[2],0)
            GPIO.output(bit[4],0)


        elif ltt in ('m' or 'M'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[1],0)
            GPIO.output(bit[4],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[1],1)
            GPIO.output(bit[4],1)


        elif ltt in ('n' or 'N'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[1],0)
            GPIO.output(bit[3],0)
            GPIO.output(bit[4],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[1],1)
            GPIO.output(bit[3],1)
            GPIO.output(bit[4],1)


        elif ltt in ('o','O'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[3],0)
            GPIO.output(bit[4],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[3],1)
            GPIO.output(bit[4],1)

        elif ltt in ('p','P'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[1],0)
            GPIO.output(bit[2],0)
            GPIO.output(bit[4],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[1],1)
            GPIO.output(bit[2],1)
            GPIO.output(bit[4],1)


        elif ltt in ('q','Q'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[1],0)
            GPIO.output(bit[2],0)
            GPIO.output(bit[3],0)
            GPIO.output(bit[4],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[1],1)
            GPIO.output(bit[2],1)
            GPIO.output(bit[3],1)
            GPIO.output(bit[4],1)


        elif ltt in ('r','R'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[2],0)
            GPIO.output(bit[3],0)
            GPIO.output(bit[4],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[2],1)
            GPIO.output(bit[3],1)
            GPIO.output(bit[4],1)


        elif ltt in ('s','S'):
            GPIO.output(bit[1],0)
            GPIO.output(bit[2],0)
            GPIO.output(bit[4],0)
            sleep(2)
            GPIO.output(bit[1],1)
            GPIO.output(bit[2],1)
            GPIO.output(bit[4],1)


        elif ltt in ('t','T'):
            GPIO.output(bit[1],0)
            GPIO.output(bit[2],0)
            GPIO.output(bit[3],0)
            GPIO.output(bit[4],0)
            sleep(2)
            GPIO.output(bit[1],1)
            GPIO.output(bit[2],1)
            GPIO.output(bit[3],1)
            GPIO.output(bit[4],1)


        elif ltt in ('u','U'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[4],0)
            GPIO.output(bit[5],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[4],1)
            GPIO.output(bit[5],1)


        elif ltt in ('v', 'V'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[2],0)
            GPIO.output(bit[4],0)
            GPIO.output(bit[5],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[2],1)
            GPIO.output(bit[4],1)
            GPIO.output(bit[5],1)


        elif ltt in ('w','X'):
            GPIO.output(bit[1],0)
            GPIO.output(bit[2],0)
            GPIO.output(bit[3],0)
            GPIO.output(bit[5],0)
            sleep(2)
            GPIO.output(bit[1],1)
            GPIO.output(bit[2],1)
            GPIO.output(bit[3],1)
            GPIO.output(bit[5],1)


        elif ltt in ('x','X'):
            GPIO.output(bit[0],0)
            GPIO.output(bit[1],0)
            GPIO.output(bit[4],0)
            GPIO.output(bit[5],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[1],1)
            GPIO.output(bit[4],1)
            GPIO.output(bit[5],1)


        elif ltt in ('y','Y') :
            GPIO.output(bit[0],0)
            GPIO.output(bit[1],0)
            GPIO.output(bit[3],0)
            GPIO.output(bit[4],0)
            GPIO.output(bit[5],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[1],1)
            GPIO.output(bit[3],1)
            GPIO.output(bit[4],1)
            GPIO.output(bit[5],1)



        elif ltt in ('z','Z') :
            GPIO.output(bit[0],0)
            GPIO.output(bit[3],0)
            GPIO.output(bit[4],0)
            sleep(2)
            GPIO.output(bit[0],1)
            GPIO.output(bit[3],1)
            GPIO.output(bit[4],1)
            GPIO.output(bit[5],1)


        elif ltt=='#':
            GPIO.output(bit[1],0)
            GPIO.output(bit[3],0)
            GPIO.output(bit[4],0)
            GPIO.output(bit[5],0)
            sleep(2)
            GPIO.output(bit[1],1)
            GPIO.output(bit[3],1)
            GPIO.output(bit[4],1)
            GPIO.output(bit[5],1)
 
    GPIO.cleanup()
    return 1

