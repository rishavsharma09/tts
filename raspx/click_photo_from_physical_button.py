
from picamera.array import PiRGBArray
import cv2
from picamera import PiCamera
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
currstate=0
prevstate=0
x=0
temp1=0
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", 
use_video_port=True):
     image=frame.array
     image=cv2.flip(image,1)
     cv2.imshow('frame',image)

     currstate=GPIO.input(18)
     if (currstate!=prevstate):
        if (currstate == 1):
                temp1=1
     else: 
        temp1=0
     prevstate=currstate
     while(temp1):
         print("photo clicked")
         cv2.imwrite("new_image.png",image)
         temp1=0
     abs=(cv2.waitKey(1) & 0xFF)
     if (abs == ord('q')):
        break
    # stream.seek(0)
     rawCapture.truncate(0)

cv2.destroyAllWindows()

