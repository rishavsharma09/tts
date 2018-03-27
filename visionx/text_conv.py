
import os
import io
import sys
from google.cloud import vision
from google.cloud.vision import types
import argparse

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='path of the image')
args=vars(ap.parse_args())

reload(sys)
sys.setdefaultencoding('utf8')

path=args["image"]

client = vision.ImageAnnotatorClient()
with io.open(path, 'rb') as image_file:
     content = image_file.read()
image = types.Image(content=content)
response = client.text_detection(image=image)
texts = response.text_annotations

print (texts[0].description)
print (texts[0].locale)

