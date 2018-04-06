import os
import time
from fun import *
font=cv2.FONT_HERSHEY_SIMPLEX

while(1):
    x=os.path.getsize('tochild.txt')
    while x<2:
        print ('l')
        x=os.path.getsize('tochild.txt')
        f=open("tochild", "r")
    if f.mode == 'r':
        contents=f.read()
        print(contents)
        f.close()
    f=open("tochild","w")
    f.truncate(0)
    f.close()
    contents = contents.replace('\n','')
    text = extract_text(contents)
    textsize = cv2.getTextSize(text, font, 1, 2)[0]
    textwidth=textsize[0]//len(text)
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
             cv2.putText(image,string,(30,30+yin*30),font,1,(0,0,0),2,cv2.LINE_AA)
         else:
         #    print(yin)
            string=text[charai:]
            cv2.putText(image,string,(30,30+yin*30),font,1,(0,0,0),2,cv2.LINE_AA)

    cv2.imwrite("temp2.png",image)
    f=open("fromchild.txt","w")
    f.write("temp2.png")
    f.close()
