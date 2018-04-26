import io
from google.cloud import translate
from google.cloud import vision
from google.cloud.vision import types
from tts import *
import numpy as np
import cv2
import os
import time
from imutils import *
font=cv2.FONT_HERSHEY_SIMPLEX

while(1):
    x=os.path.getsize('tochild.txt')
    while x<2:
        print ('l')
        x=os.path.getsize('tochild.txt')
    f=open("tochild.txt", "r")
    if f.mode == 'r':
        contents=f.read()
        print(contents)
        f.close()
    f=open("tochild.txt","w")
    f.truncate(0)
    f.close()
    image=np.ones([480,800,3],dtype=np.uint8)
    contents = contents.replace('\n','')
    x=os.path.getsize('fulltext.txt')
    if x >2:    
        f=open("fulltext.txt","w")
        f.truncate(0)
        f.close()
    else :
        pass
    extract_text(contents)
    x=os.path.getsize('fulltext.txt')
    while x<2:
        print ('l')
        x=os.path.getsize('fulltext.txt')
    f=open("fulltext.txt", "r")
    if f.mode == 'r':
        text=f.read()
        print(text)
        f.close()
    f=open("fulltext.txt","w")
    f.truncate(0)
    f.close()
    text=text.replace('\n','')
    print (text)
    textsize = cv2.getTextSize(text, font, 1, 2)[0]
    textwidth=13
    y=textsize[0]//image.shape[0]
    textsze=textsize[0]//textwidth
    charaf=image.shape[0]//textwidth
    x=charaf
    charai=0
    for yin in range(0,y):
        # print("for")
         if textsze-charaf>0:
             string=text[charai:charaf]
             charai=charaf
             charaf=x+charaf
             print(charaf)
             
cv2.putText(image,string,(30,30+yin*30),font,1,(255,255,255),2,cv2.LINE_AA)
         else:
         #    print(yin)
            string=text[charai:]
            
cv2.putText(image,string,(30,30+yin*30),font,1,(255,255,255),2,cv2.LINE_AA)

    cv2.imwrite("temp2.png",image)
    f=open("fromchild.txt","w")
    f.write("temp2.png")
    f.close()

