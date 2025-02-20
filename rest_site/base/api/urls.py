from django.urls import path
from . import views

urlpatterns = [
    path('',views.routes,name='routes'),
    path('students/',views.getStudents,name='getStudents'),
]