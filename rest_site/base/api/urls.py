from django.urls import path
from . import views


urlpatterns = [
    path('allstudents/',views.get_all_students,name='getallStudents'),
    path('createstudents/',views.create_students,name='createStudents'),
]