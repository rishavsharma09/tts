# -*- coding: utf-8 -*-
from google.cloud import translate
from google.cloud import vision
from google.cloud.vision import types
import io



def translate_text_(text,target='en'):
    translate_client=translate.Client()

    result = translate_client.translate(
       text, target_language='en')

   # print('Text: {}'.format(result['input']))
    x=result['translatedText']
    f=open("fulltext.txt","w")
    f.write(x)
    f.close()
    #print('Detected source language: {}'.format(
#        result['detectedSourceLanguage']))


def extract_text_(path):
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
         content = image_file.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)

    texts = response.text_annotations
    translate_text_(texts[0].description)

    #print texts[0].description
    #print texts[0].locale




