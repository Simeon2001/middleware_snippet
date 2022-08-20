def listen(request, response):
    verb = request.method
    path = request.path
    status = response.status_code
    duration = "0.34"
    payload = request.body
    header = request.headers
    resp = response.data
    print(verb)
    print(path)
    print(status)
    print(duration)
    print(payload)
    print(header)
    print(resp)
    return True