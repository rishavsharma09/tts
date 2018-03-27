import cv2
import argparse
ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="add aimage")
ap.add_argument("-r", "--rotation", required=False, help="want to rotate 
image")

args=vars(ap.parse_args())

image=cv2.imread(args['image'])
font=cv2.FONT_HERSHEY_SIMPLEX
text="RR"
# get boundary of this text
textsize = cv2.getTextSize(text, font, 1, 2)[0]
textwidth=textsize[0]//len(text)
#print (textwidth)
#print("textsize",textsize[0])
#print("imageshape",image.shape[0])
y=textsize[0]//image.shape[0]
#print(y)
print('y',y)
textsze=textsize[0]//textwidth
charaf=image.shape[0]//textwidth
#print(textsze)
#print(charaf)
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


cv2.imshow("hey",image)

if (cv2.waitKey(0) & 0xFF) == ord('c'):
    cv2.destroyAllWindows()



