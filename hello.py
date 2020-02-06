def application(env, start_response):
    print(env)
    l = env['QUERY_STRING'].split('&')
    l = [(i+'\n').encode() for i in l]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return l
