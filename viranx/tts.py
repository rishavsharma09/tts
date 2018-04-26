# -*- coding: utf-8 -*-
import os
import io
from google.cloud import translate
from google.cloud import vision
from google.cloud.vision import types

def translate_text(text,target='en'):
    translate_client=translate.Client()

    result = translate_client.translate(
        text, target_language='en'
    x=result['translatedText']
    f=open("fulltext.txt","w")
    f.write(x)
    f.close()




def extract_text(path):
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
         content = image_file.read()
    image = types.Image(content=content)
    response = client.document_text_detection(image=image)
    
    texts = response.full_text_annotation
    translate_text(texts.text)

    #print texts[0].description
    #print texts[0].locale



