import json
import boto3
import os
import sys

def ipa_to_audio(event, context):
    # init polly
    client = boto3.client('polly', region_name='us-east-1')

    # parse event for body
    body = json.loads(event['body'])

    # extract inputs from body
    ipa = body['ipa']
    contentType = body['contentType']

    # synthesize speech
    response = client.synthesize_speech(Engine='standard',
        LanguageCode='en-US',
        OutputFormat=contentType,
        Text="<phoneme alphabet='ipa' ph='/" + ipa + "/'></phoneme>",
        TextType='ssml',
        VoiceId='Joey')

    # parse response
    return response['AudioStream'].read() # temporary

def test(args):
    if len(sys.argv) == 3:
        event, context = sys.argv[1:3]
    elif len(sys.argv) > 1:
        event = sys.argv[1]
    else:
        event = {'version': '2.0', 'routeKey': 'POST /', 'rawPath': '/', 'rawQueryString': '', 'headers': {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'cache-control': 'no-cache', 'content-length': '62', 'content-type': 'application/json', 'host': '5qyc48nn1k.execute-api.us-east-1.amazonaws.com', 'postman-token': '96d17268-86ff-42f0-bb35-a81a9cac185e', 'user-agent': 'PostmanRuntime/7.32.2', 'x-amzn-trace-id': 'Root=1-647f8367-3c0a252b3e9bcac606c39fdd', 'x-forwarded-for': '54.86.50.139', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https'}, 'requestContext': {'accountId': '791244022196', 'apiId': '5qyc48nn1k', 'domainName': '5qyc48nn1k.execute-api.us-east-1.amazonaws.com', 'domainPrefix': '5qyc48nn1k', 'http': {'method': 'POST', 'path': '/', 'protocol': 'HTTP/1.1', 'sourceIp': '54.86.50.139', 'userAgent': 'PostmanRuntime/7.32.2'}, 'requestId': 'GHF4PjCmoAMEVzQ=', 'routeKey': 'POST /', 'stage': '$default', 'time': '06/Jun/2023:19:05:11 +0000', 'timeEpoch': 1686078311622}, 'body': '{\r\n    "ipa": "kənˈkluːʒən",\r\n    "contentType": "mp3"\r\n}', 'isBase64Encoded': False}
        context = 0 # LambdaContext([aws_request_id=fc5a4b88-b7e9-4aba-84ae-75ce7623ca3d,log_group_name=/aws/lambda/ipa-to-audio-dev-ipa_to_audio,log_stream_name=2023/06/06/[$LATEST]17d2c4f9af4e407db141bb824085b976,function_name=ipa-to-audio-dev-ipa_to_audio,memory_limit_in_mb=1024,function_version=$LATEST,invoked_function_arn=arn:aws:lambda:us-east-1:791244022196:function:ipa-to-audio-dev-ipa_to_audio,client_context=None,identity=CognitoIdentity([cognito_identity_id=None,cognito_identity_pool_id=None])])
    print(ipa_to_audio(event, context))

if __name__ == "__main__":
    test(sys.argv)
