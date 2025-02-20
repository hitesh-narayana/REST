from django.http import JsonResponse

def routes(request):
    routes = [
        'GET /api/students',
        'GET /api/students/:id',
    ]
    return JsonResponse(routes, safe=False)
