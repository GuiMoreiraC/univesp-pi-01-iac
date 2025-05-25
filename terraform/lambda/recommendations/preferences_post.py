
import json
import boto3

s3 = boto3.client('s3')
BUCKET = "conteudo-audiovisual-data"

def lambda_handler(event, context):
    try:
        prefs = json.loads(event['body'])
        s3.put_object(Bucket=BUCKET, Key='preferences.json', Body=json.dumps(prefs))
        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps(prefs)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({ 'error': str(e) })
        }
