def application(env, start_response):
    print(env)
    l = env['QUERY_STRING'].split('&')
    l = [(i+'\n').encode() for i in l]
    start_responce('200 OK', [('Content-Type', 'text/html')])
    return l
