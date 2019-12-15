from cgi import parse_qs

def application(environ, start_response):

    query = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    body = []
    for k,v in query.items():
        for i in v:
            body.append(k +'=' + i +'/r/n/')

    status = '200 OK'
    headers = [
        ('Content-Type','text/plain')
        ]
    start_response(status, headers)
    return body
        
