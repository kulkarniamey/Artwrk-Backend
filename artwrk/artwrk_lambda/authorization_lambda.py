import jwt
import boto3
import json

def generatePolicy(principalId, effect, methodArn):
    
    authResponse = {}
    authResponse['principalId'] = principalId
 
    if effect and methodArn:
        policyDocument = {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Sid': 'FirstStatement',
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': methodArn
                }
            ]
        }

        authResponse['policyDocument'] = policyDocument
 
    return authResponse
 

def lambda_handler(event, context):    
    token = event['authorization_token']  
    if not token:
        return {
        'statusCode': 404,
        'body': "Token not Found.Please login again!"
        }
    try:
        jwt.decode(token, 'secret', algorithms=['HS256'])
        generatePolicy('user','Allow',event['methodArn'])
    except Exception as e:
        print(e)
        generatePolicy('user','Deny',event['methodArn'])
        return {
        'statusCode': 401,
        'body': "Invalid Token.Please login again!"
        }
        