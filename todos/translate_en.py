import os
import json

from todos import get
import boto3

translate = boto3.client('translate')

def translate_en(event, context):
    result = get.get(event, context)

    dict_result = json.loads(result)

    idValue = dict_result["id"]

    idValue_translated = translate.translate_text(Text=idValue, SourceLanguageCode="es", TargetLanguageCode="en")

    dict_result['id'] = idValue_translated

    # create a response
    response = {
            "statusCode": 200,
            "body": json.dumps(dict_result['Item'],
                                cls=decimalencoder.DecimalEncoder)
    }

    return response
