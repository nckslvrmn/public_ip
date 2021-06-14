def handler(event, _):
    client_ip = event.get('headers', {}).get('x-forwarded-for').split(',')[0]
    response_code = 200

    if client_ip is None:
        body = 'couldnt retrieve public IP from x-forwarded-for header'
        content_type = 'text/plain'
        response_code = 500
    elif event.get('queryStringParameters', {}).get('format') == 'json':
        body = f'{ "ip": "{client_ip}" }'
        content_type = 'application/json'
    else:
        body = client_ip
        content_type = 'text/plain'

    return {
        'statusCode': response_code,
        'headers': {
            'Content-Type': content_type,
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': 0
        },
        'body': body
    }
