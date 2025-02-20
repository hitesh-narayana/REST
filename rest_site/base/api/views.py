from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def routes(request):
    routes = [
        'GET /api/',
        'GET /api/students',

    ]
    return Response(routes)
