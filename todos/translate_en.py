import os
import json

from todos import get
import boto3

translate = boto3.client('translate')

def translate_en(event, context):
    result = get.get(event, context)

    idValue = result['id']
    #result_translated = translate.translate_text(Text=result, SourceLanguageCode="es", TargetLanguageCode="en")

    #return result_translated
    return idValue
