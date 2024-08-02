from django.http import HttpResponse


class HealthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.headers._store)
        if request.path == "/healthz":
            return HttpResponse("ok")
        return self.get_response(request)
