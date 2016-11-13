import urlparse

def app(environ, start_response):
    data = ''
    params = environ['QUERY_STRING'].split('&')
    for line in params:
        data += line + '\n'
    
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])