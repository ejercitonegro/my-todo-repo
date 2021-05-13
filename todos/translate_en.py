import os
import json
import codecs

#from todos import get
import boto3

translate = boto3.client('translate')

def translate_en(event, context):
    #result = get.get(event, context)
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
           'id': event['pathParameters']['id']
        }
    )

    translated = translate.translate_text(Text=result['Item']['text'], SourceLanguageCode='auto', TargetLanguageCode='es')
    result['Item']['text'] = translated['TranslatedText']

    # create a response
    response = {
        "statusCode": 200,
         "body": json.dumps(result['Item'], cls=decimalencoder.DecimalEncoder)
    }

    return response
