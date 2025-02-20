from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Student

# Create your views here.

def home(request):
    students = Student.objects.all()
    context  = {'students':students}
    return render(request,'home.html',context)
