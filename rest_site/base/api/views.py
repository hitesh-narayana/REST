from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Student
from base.api.serializers import StudentSerializer
from django.shortcuts import get_object_or_404



@api_view(['GET'])
def getallStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudent(request,pk):
    student = get_object_or_404(id=pk)
    serializer = StudentSerializer(student,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createStudent(request):
    data = request.data
    name = data.get('name', None)
    city = data.get('city', None)

    if not name or not city:
        return Response({"error": "Name and City are required"}, status=400)

    student = Student.objects.create(name=name, city=city)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)
