def handler(event, _):
    x_fwd = event.get('headers', {}).get('x-forwarded-for')

    if x_fwd is None:
        return response(
            500,
            'text/plain',
            'couldnt retrieve public IP'
        )

    client_ip = x_fwd.split(',')[0]
    if event.get('queryStringParameters', {}).get('format') == 'json':
        return response(
            200,
            'application/json',
            f'{{"ip":"{client_ip}"}}'
        )

    return response(
        200,
        'text/plain',
        client_ip
    )


def response(response_code, content_type, body):
    return {
        'statusCode': response_code,
        'headers': {
            'Content-Type': content_type,
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': 0
        },
        'body': f'{body}\n'
    }
