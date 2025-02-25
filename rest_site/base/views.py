from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Student
from .forms import StudentForm

# Create your views here.

def home(request):
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request,'home.html',context)

def add(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form
    }
    return render(request,'add_student.html',context)
