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

    for i in result:
        for key in i:
            if key=="text":
                value = i[key]
                translated = translate.translate_text(Text=value, SourceLanguageCode='auto', TargetLanguageCode='es')
                i[key] = translated['TranslatedText']

    # create a response
    response = {
        "statusCode": 200,
         "body": json.dumps(result['Item'], cls=decimalencoder.DecimalEncoder)
    }

    return response
