import json
import boto3
import os

def lambda_handler(event, context):
    input = event['ipa']
    response = client.synthesize_speech(Engine='standard',
        LanguageCode='en-US',
        OutputFormat=event['contentType'],
        Text="<phoneme alphabet='ipa' ph='/" + input + "/'></phoneme>",
        TextType='ssml',
        VoiceId='Joey')
    return response

def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

