
def app(environ, start_response):
    """Simplest possible application object"""
    data = b'Hello, World!\n'
    status = '200 OK'
    # resp = {}
    len_msg = 0
    resp_1 = []
    for key in environ.keys():
        resp_1.append(((str(key) + ': ') + (str(environ.get(key)) + '\n')).encode('utf-8'))
        len_msg += len(str(key)) + len(str(environ.get(key))) + 5
    qs = (environ.get('QUERY_STRING', None)).split('&')
    for i in range(len(qs)):
        qs[i] = (str(qs[i]) + '\n').encode('utf-8')
        len_msg += len(qs[i])
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len_msg))
    ]
    start_response(status, response_headers)
    return iter(qs)
