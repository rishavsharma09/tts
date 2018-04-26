import numpy as np 
from picamera.array import PiRGBArray
import cv2
from picamera import PiCamera
import time
import RPi.GPIO as GPIO
import os
from funct import *
GPIO.setmode(GPIO.BCM)
currstate=0
prevstate=0
x=0
temp1=0
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
display=np.zeros([480,800,3],dtype=np.uint8)
camera = PiCamera()
camera.resolution = (800, 480)
camera.framerate = 25
rawCapture = PiRGBArray(camera, size=(800, 480))
#imaga=np.ones([380,540,3],dtype=np.uint8)

def imshow(image):
    cv2.imshow("frame",image)

time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", 
use_video_port=True):
     image=frame.array
    # image=cv2.flip(image,0)
     #image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
     display[:,:,:]=image[:,:,:]
 #    display=cv2.cvtColor(display,cv2.COLOR_RGB2BGR)
     currstate=GPIO.input(18)
     if (currstate!=prevstate):
        if (currstate == 1):
                temp1=1
     else: 
        temp1=0
     prevstate=currstate
     while(temp1):
         print("photo clicked")
         cv2.imwrite("temp.png",image)
         temp1=0
         display.fill(0)
         imshow(display)
         cv2.waitKey(1)
         f=open("tochild.txt","w")
         f.write("temp.png")
         f.close()
         x=os.path.getsize("fromchild.txt")
         print(x)
         while x<2:
             print("x")
             x=os.path.getsize("fromchild.txt")
         f=open("fromchild.txt","r")
         if f.mode=='r':
             contents=f.read()
             print(contents)
             f.close()
         f=open("fromchild.txt","w")
         f.truncate(0)
         f.close()
         contents=contents.replace('\n','')
         tima=cv2.imread(contents)
         imshow(tima)
         display[:,:,:]=tima[:,:,:]
         imshow(display)
         cv2.waitKey(1)
         toexit=GPIO.input(18)
         
         while(toexit==0):
             print("iamwaitingtext")
             toexit=GPIO.input(18)
             tospeech=GPIO.input(15)
             todisp=GPIO.input(17)
             if (tospeech==1):
                 toexit=speakfulltext()
             if (todisp==1):
                 toexit=displaytext()
         display.fill(0)
     abs=(cv2.waitKey(1) & 0xFF)
     if (abs == ord('q')):
        break
    # stream.seek(0)
     
     imshow(display)
     cv2.waitKey(1)
     rawCapture.truncate(0)
cv2.destroyAllWindows()


