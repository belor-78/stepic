def application(env, start_response):
    l = env[QUERY_STRING].split('&')
    l = [i+'\n' for i in l]
    start_responce('200 OK', [('Content-Type', 'text/html')])
    return l
