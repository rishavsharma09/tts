
# -*- coding: utf-8 -*-
import os
import io
from google.cloud import vision
from google.cloud.vision import types
import argparse
import base64

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='path of the image')
args=vars(ap.parse_args())


path=args["image"]
client = vision.ImageAnnotatorClient()
with io.open(path, 'rb') as image_file:
     content=image_file.read()
image = types.Image(content=content)
response = client.document_text_detection(image=image)
print('Labels:')
texts = response.full_text_annotation
print(texts.text)

