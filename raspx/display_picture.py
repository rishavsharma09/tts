
import cv2
import argparse
ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="add aimage")
ap.add_argument("-r", "--rotation", required=False, help="want to rotate image")

args=vars(ap.parse_args())

image=cv2.imread(args['image'])
(h,w)=image.shape[:2]
center=(w/2,h/2)
args['rotation']=0
x=float(args['rotation'])
m=cv2.getRotationMatrix2D(center,x,1.0)
rotated=cv2.warpAffine(image,m,(w,h))
cv2.imshow("hey",rotated)

if (cv2.waitKey(0) & 0xFF) == ord('c'):
    cv2.destroyAllWindows()
