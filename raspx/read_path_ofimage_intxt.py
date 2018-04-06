import cv2
import time
import os
x=os.path.getsize('imagetoc.txt')
print (x)
while x<2:
    time.sleep(0.1)
    x=os.path.getsize('imagetoc.txt')
f=open("imagetoc.txt", "r")
if f.mode == 'r':
    contents=f.read()
    print(contents)
    f.close()
f=open("imagetoc.txt","w")
f.truncate(0)
f.close()
contents = contents.replace('\n','')
image=cv2.imread(contents)
cv2.imshow('hey',image)
if (cv2.waitKey(0) & 0xFF) == ord('c'):
    cv2.destroyAllWindows()


