from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Student

@api_view(['GET'])
def routes(request):
    routes = [
        'GET /api/',
        'GET /api/students',
    ]
    return Response(routes)

@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    return Response(students)