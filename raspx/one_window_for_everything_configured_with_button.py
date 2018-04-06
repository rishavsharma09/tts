import numpy as np 
from picamera.array import PiRGBArray
import cv2
from picamera import PiCamera
import time
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BCM)
currstate=0
prevstate=0
temp=0
x=0
temp1=0
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
display=np.zeros((768,768,3),dtype=np.uint8)
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", 
use_video_port$
     image=frame.array
     image=cv2.flip(image,1)
     #image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
     display[44:524,192:832,:]=image[:,:,:]
 #    display=cv2.cvtColor(display,cv2.COLOR_RGB2BGR)
     cv2.imshow('frame',display)

     currstate1=GPIO.input(18)
     if (currstate1!=prevstate1):
        if (currstate1 == 1):
                temp1=1
     else: 
        temp1=0
     prevstate1=currstate1
     while(temp1):
         print("photo clicked")
         cv2.imwrite("temp.png",image)
         display[44:524,192:832,:]=0
         f=open("tochild","w")
         f.write("temp.png")
         f.close()
         x=os.path.getsize('fromchild.txt')
         while x<2:
            print ('l')
            x=os.path.getsize('fromchild.txt')
        f=open("fromchild", "r")
        if f.mode == 'r':
            contents=f.read()
            print(contents)
            f.close()
        f=open("fromchild","w")
        f.truncate(0)
        f.close()
        contents = contents.replace('\n','')
        image=cv2.imread(contents)
        display[44:524,192:832,:]=image[:,:,:]
        t oexit=GPIO.input(17)
        temp1=0
        while(toexit==0):
            print("iamwaitingtexit")
            toexit=GPIO.input(17)
     abs=(cv2.waitKey(1) & 0xFF)
     if (abs == ord('q')):
        break
    # stream.seek(0)
     rawCapture.truncate(0)
cv2.destroyAllWindows()


