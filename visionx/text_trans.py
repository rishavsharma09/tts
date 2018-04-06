
# -*- coding: utf-8 -*-
from google.cloud import translate

def translate_text(text,target='en'):
    translate_client=translate.Client()

    result = translate_client.translate(
        text, target_language='en')

    print('Text: {}'.format(result['input']))
    print('Translation: {}'.format(result['translatedText']))
    print('Detected source language: {}'.format(
        result['detectedSourceLanguage']))
    
example_text='''इनपुट उपकरण आपके 
द्वारा चुनी गई भाषा में 
वेब पर कहीं भी लिखना 
आसान बनाता है. और जानें

इसे आज़माने के लिए, 
नीचे अपनी भाषा और 
इनपुट उपकरण चुनें और 
लिखना आरंभ करें.'''
translate_text(example_text)
