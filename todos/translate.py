import os
import json
import boto3
from todos import decimalencoder

# Cliente 'translate' de la API 
translateb = boto3.client('translate')
# Recurso 'dynamodb' de la API
dynamodb = boto3.resource('dynamodb')

# Funcion tranlate
## Traduce el campo text del resultado devuelto de la consulta a la DB
def translate(event, context):

    # Generamos objeto table de la clase dynamodb con el nombre de la tabla obtenido de las variables de entorno
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # Obtenemos el item de la tabla a partir del identificador
    result = table.get_item(
        Key={
           'id': event['pathParameters']['id']
        }
    )

    # Traducimos el campo text del resultado obtenido en la consulta a la tabla.
    # Idioma origen -> autotedectado
    # Idioma deseado -> se obtiene de la url y se pasa como parametro
    translated = translateb.translate_text(Text=result['Item']['text'], SourceLanguageCode='auto', TargetLanguageCode=event['pathParameters']['lang'])

    # Se sustituye por el valor del resultado traducido
    result['Item']['text'] = translated['TranslatedText']

    # Generamos la respuesta a devolver
    response = {
        "statusCode": 200,
         "body": json.dumps(result['Item'], cls=decimalencoder.DecimalEncoder)
    }

    return response
