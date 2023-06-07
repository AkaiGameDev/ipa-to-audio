import json
import boto3
import os

def ipa_to_audio(event, context):
    client = boto3.client('polly')
    body = json.loads(event['body'])
    ipa = body['ipa']
    response = client.synthesize_speech(Engine='standard',
        LanguageCode='en-US',
        OutputFormat=body['contentType'],
        Text="<phoneme alphabet='ipa' ph='/" + ipa + "/'></phoneme>",
        TextType='ssml',
        VoiceId='Joey')
    data = response['AudioStream'].read()
    return data
