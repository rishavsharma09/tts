# -*- coding: utf-8 -*-
import os
import io
from google.cloud import translate
from google.cloud import vision
from google.cloud.vision import types
import argparse
ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='path of the image')
args=vars(ap.parse_args())

def translate_text(text,target='en'):
    translate_client=translate.Client()

    result = translate_client.translate(
        text, target_language='en')


    print('Text: {}'.format(result['input']))
    print('Translation: {}'.format(result['translatedText']))
    print('Detected source language: {}'.format(
        result['detectedSourceLanguage']))




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


extract_text(args["image"])

