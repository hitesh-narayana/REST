from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Student
from base.api.serializers import StudentSerializer

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
    serializer = StudentSerializer(students,many=True)
    return Response(serializer.data)