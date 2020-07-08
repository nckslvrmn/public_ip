import json

def handler(event, context):
    client_ip = event['headers']['x-forwarded-for'].split(',')[0]
    if event['queryStringParameters']['format'] == 'json':
        body = json.dumps({ 'ip': client_ip })
        content_type = 'application/json'
    else:
        body = client_ip
        content_type = 'text/plain'

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': content_type,
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': 0
        },
        'body': body
    }
