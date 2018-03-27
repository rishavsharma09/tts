 
from picamera.array import PiRGBArray
import cv2
from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
     image=frame.array
     image=cv2.flip(image,1)
     cv2.imshow('frame',image)
     abs=(cv2.waitKey(1) & 0xFF)
     if (abs == ord('c')):
        camera.capture(rawCapture,format='bgr')
        image=rawCapture.array
        cv2.imwrite("new_image.png",image)
        print("photo is clicked")
    
     if (abs == ord('q')):
        break
    # stream.seek(0)
     rawCapture.truncate(0)

cv2.destroyAllWindows()













































