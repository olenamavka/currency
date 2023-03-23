from time import time

from currency.models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()

        response = self.get_response(request)

        end = time()
        execution_time = end - start
        RequestResponseLog.objects.create(
            request_method=request.method,
            path=request.path,
            time=execution_time
        )
        return response
