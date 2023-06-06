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
