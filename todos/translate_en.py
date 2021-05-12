import os
import json

from todos import get
import boto3

translate = boto3.client('translate')

def translate_en(event, context):
    #result = get.get(event, context)

    json_string = """
    [
        {
            "checked": false,
            "createdAt": "1620823279.6609614",
            "text": "texto en español",
            "id": "59c8f383-b31f-11eb-9179-a5009fe4c60e",
            "updatedAt": "1620823279.6609614"
        }
    ]
    """

    result = json.loads(result)

    #idValue = dict_result["id"]

    #idValue_translated = translate.translate_text(Text=idValue, SourceLanguageCode="es", TargetLanguageCode="en")

    #dict_result['id'] = idValue_translated

    # create a response
    response = {
            "statusCode": 200,
            "body": json.dumps(result['Item'],
                                cls=decimalencoder.DecimalEncoder)
    }

    return response
