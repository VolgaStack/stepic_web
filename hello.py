from urlparse import urlparse

def hello(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    for key in d:
        for value in d[key]:
            data += key + '=' + value + '\r\n'
    
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])