import os
import json

from todos import get
import boto3

translate = boto3.client('translate')


def translate_en(event, context):
    result=get.get
    return result
