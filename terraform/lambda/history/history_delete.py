
import json
import boto3

s3 = boto3.client('s3')
BUCKET = "conteudo-audiovisual-data"

def lambda_handler(event, context):
    try:
        history_id = int(event['pathParameters']['id'])
        result = s3.get_object(Bucket=BUCKET, Key='history.json')
        history = json.loads(result['Body'].read().decode('utf-8'))

        new_history = [item for item in history if item['id'] != history_id]

        if len(new_history) == len(history):
            return { 'statusCode': 404, 'body': json.dumps({ 'error': 'ID not found' }) }

        s3.put_object(Bucket=BUCKET, Key='history.json', Body=json.dumps(new_history))
        return { 'statusCode': 204 }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({ 'error': str(e) })
        }
