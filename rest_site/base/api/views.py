from django.http import JsonResponse

def routes(request):
    routes = [
        'GET /api/students',
    ]
    return JsonResponse(routes, safe=False)
