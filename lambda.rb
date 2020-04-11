require 'json'

def handler(event:, context:)
  client_ip = event['headers']['x-forwarded-for'].split(',').first
  if event['queryStringParameters']['format'] == 'json'
    body = JSON.generate(ip: client_ip)
    type = 'application/json'
  else
    body = client_ip
    type = 'text/plain'
  end

  {
    statusCode: 200,
    headers: {
      'Content-Type': type,
      'Cache-Control': 'no-cache, no-store, must-revalidate',
      'Pragma': 'no-cache',
      'Expires': 0
    },
    body: body
  }
end
