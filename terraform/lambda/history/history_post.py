
import json
import boto3

s3 = boto3.client('s3')
BUCKET = "conteudo-audiovisual-data"

def lambda_handler(event, context):
    try:
        new_item = json.loads(event['body'])
        result = s3.get_object(Bucket=BUCKET, Key='history.json')
        history = json.loads(result['Body'].read().decode('utf-8'))

        new_id = max([item['id'] for item in history], default=0) + 1
        new_item['id'] = new_id
        history.append(new_item)

        s3.put_object(Bucket=BUCKET, Key='history.json', Body=json.dumps(history))
        return {
            'statusCode': 201,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps(new_item)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({ 'error': str(e) })
        }
