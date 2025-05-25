
import json
import boto3

s3 = boto3.client('s3')
BUCKET = "conteudo-audiovisual-data"

def lambda_handler(event, context):
    try:
        hist_res = s3.get_object(Bucket=BUCKET, Key='history.json')
        history = json.loads(hist_res['Body'].read().decode('utf-8'))

        try:
            pref_res = s3.get_object(Bucket=BUCKET, Key='preferences.json')
            prefs = json.loads(pref_res['Body'].read().decode('utf-8'))
        except:
            prefs = {}

        rel_res = s3.get_object(Bucket=BUCKET, Key='releases.json')
        releases = json.loads(rel_res['Body'].read().decode('utf-8'))

        if prefs.get('favoriteGenres'):
            releases = [r for r in releases if any(g in prefs['favoriteGenres'] for g in r.get('genres', []))]
        if prefs.get('favoritePlatforms'):
            releases = [r for r in releases if r.get('platform') in prefs['favoritePlatforms']]

        recommendations = releases[:5]

        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps(recommendations)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({ 'error': str(e) })
        }
