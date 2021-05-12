import os
import json

from todos import get
import boto3

translate = boto3.client('translate')

def translate_en(event, context):
    #result = get.get(event, context)


    #result = json.loads(result)

    #idValue = dict_result["id"]

    #idValue_translated = translate.translate_text(Text=idValue, SourceLanguageCode="es", TargetLanguageCode="en")

    #dict_result['id'] = idValue_translated

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'], cls=decimalencoder.DecimalEncoder)
    }
    
    return response
