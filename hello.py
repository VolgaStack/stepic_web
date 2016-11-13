import urlparse

def app(environ, start_response):
    params = urlparse.parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    for key, value in params.iteritems():
        data += key + '=' + value + '\r\n'
    
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])