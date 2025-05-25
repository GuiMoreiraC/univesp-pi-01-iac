
import json
import boto3

s3 = boto3.client('s3')
BUCKET = "conteudo-audiovisual-data"

def lambda_handler(event, context):
    try:
        result = s3.get_object(Bucket=BUCKET, Key='history.json')
        history_data = json.loads(result['Body'].read().decode('utf-8'))

        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps(history_data)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({ 'error': str(e) })
        }
