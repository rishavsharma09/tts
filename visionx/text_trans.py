
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
    
example_text='''好一朵美丽的茉莉花
好一朵美丽的茉莉花
芬芳美丽满枝極
又香又白人人夸
让我来将你摘下
送给别人家
茉莉花呀茉莉花'''

translate_text(example_text)
