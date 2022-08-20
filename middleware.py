from .call_request import listen

# Listen middleware

class ListenMiddleware:
    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        listen(request, response)

        return response
