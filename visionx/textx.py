
import io
import os
import base64

from google.cloud import vision
from google.cloud.vision import types

vision_client = vision.ImageAnnotatorClient()
file_name = 'jip.png'

with io.open(file_name,'rb') as image:
    image_content = image.read()
    
