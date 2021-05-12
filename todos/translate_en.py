import os
import json

from todos import get
import boto3

translate = boto3.client('translate')

def translate_en(event, context):
    result = get.get(event, context)

    idValue = result[0]['id']
    idValue_translated = translate.translate_text(Text=idValue, SourceLanguageCode="es", TargetLanguageCode="en")
    result[0]['id'] = idValue_translated

    return result_translated
