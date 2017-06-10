# public_ip
Returns your public IP using only the nginx configuration file.

This also has support for returning a JSON response via a url parameter. To get the json response, simply do:

```
curl http://example.com?format=json
```

otherwise, for plaintext response, no url parameter is needed.
