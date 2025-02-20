from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Student
from base.api.serializers import StudentSerializer


@api_view(['GET'])
def getallStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudent(request,pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student,many=False)
    return Response(serializer.data)