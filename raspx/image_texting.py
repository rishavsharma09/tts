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
print (textsize[0])
print (textsize[1])
# get coords based on boundary
textX = (image.shape[1] - textsize[0]) // 2
textY = (image.shape[0] + textsize[1]) // 2

cv2.putText(image,text,(textX,textY),font,1,(0,0,0),2,cv2.LINE_AA)
cv2.imshow("hey",image)

if (cv2.waitKey(0) & 0xFF) == ord('c'):
    cv2.destroyAllWindows()



