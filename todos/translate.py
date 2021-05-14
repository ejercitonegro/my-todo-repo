import os
import json
import boto3
from todos import decimalencoder

translate = boto3.client('translate')
dynamodb = boto3.resource('dynamodb')

def translate(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
           'id': event['pathParameters']['id']
        }
    )

    translated = translate.translate_text(Text=result['Item']['text'], SourceLanguageCode='auto', TargetLanguageCode=event['pathParameters']['lang'])
    result['Item']['text'] = translated['TranslatedText']

    # create a response
    response = {
        "statusCode": 200,
         "body": json.dumps(result['Item'], cls=decimalencoder.DecimalEncoder)
    }

    return response
