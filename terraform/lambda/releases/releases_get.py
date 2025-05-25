
import json
import boto3

s3 = boto3.client('s3')
BUCKET = "conteudo-audiovisual-data"

def lambda_handler(event, context):
    try:
        result = s3.get_object(Bucket=BUCKET, Key='releases.json')
        releases = json.loads(result['Body'].read().decode('utf-8'))

        params = event.get('queryStringParameters') or {}
        if 'platform' in params:
            releases = [r for r in releases if r.get('platform') == params['platform']]
        if 'genre' in params:
            releases = [r for r in releases if 'genres' in r and params['genre'] in r['genres']]
        if 'startDate' in params:
            releases = [r for r in releases if r.get('releaseDate') >= params['startDate']]
        if 'endDate' in params:
            releases = [r for r in releases if r.get('releaseDate') <= params['endDate']]

        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps(releases)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({ 'error': str(e) })
        }
