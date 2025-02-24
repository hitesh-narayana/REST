from django.urls import path
from . import views


urlpatterns = [
    path('allstudents/',views.getallStudents,name='getallStudents'),
    path('student/<str:pk>/',views.getStudent,name='getStudent'),
    path('createstudent/',views.createStudent,name='createStudent'),
]