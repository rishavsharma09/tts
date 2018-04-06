#---------library files--------#

#.....picam.....#
from picamera.array import PiRGBArray
import cv2
from picamera import PiCamera
#.....picam.....#

#.....raspOS.....#
import time
#.....raspOS.....#

#.....GPIO_lib.....#
import RPi.GPIO as GPIO
from gpiozero import  Button 
from time import sleep
#.....GPIO_lib.....#


#--------camera setup---------#
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
#--------camera setup---------#

#--------GPIO_setup-----------#
#pin=[18,23,24]  # pin 18,23,24 are assigned to cick, saveyes, saveno
click = Button(17)
exitt = Button(23)
#GPIO.setmode(GPIO.BCM)

#GPIO.setup(x[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(x[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(x[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#-------GPIO_setup-----------#
img1=cv2.imread('img1')
img2=cv2.imread('img2')
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
     image=frame.array
     image=cv2.flip(image,1)
     cv2.imshow('frame',image)
     click.wait_for_press()
     camera.capture(rawCapture,format='bgr')
     image=rawCapture.array
     cv2.imwrite('tempforchild.png',image)
     f=open('forchild.text','w')
     f.write('tempforchild.png')
     f.close()
     text_chk_from_child=os.path.getsize('textfromchild.txt')
     while x<2:
            cv2.imshow('frame'img1)
            time.sleep(0.1)
            cv2.imshow('frame',img2)
            x=os.path.getsize('textfromchid.txt')
     f=open("textfromchild",'r')
     if f.mode=='r':
            contents=f.read()
            #print(contents)
            f.truncate(0)
            f.close()
     contents=contents.replace('/n','')
     image=cv2.imread(contents)
     cv2.imshow('final_text',image)
     exitt.wait_for_press()
     rawCapture.truncate(0)
cv2.destroyAllWindows()
