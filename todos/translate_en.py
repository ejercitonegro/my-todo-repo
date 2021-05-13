import os
import json
import codecs

from todos import get
import boto3

translate = boto3.client('translate')

def translate_en(event, context):
    result = get.get(event, context)

    for i in result:
        for key in i:
            if key=="text":
                value = i[key]
                translated = translate.translate_text(Text=value, SourceLanguageCode='auto', TargetLanguageCode='es')
                i[key] = translated

    return result
