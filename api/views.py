from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from .models import Student, School
from .serializer import StudentSerializer as student_serializer
from .serializer import SchoolSerializer as school_serializer
from rest_framework.response import Response
class Studentviewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = student_serializer
    # serializer = student_serializer





class Schoolviewset(viewsets.ModelViewSet):
    queryset = School.objects.all()

    serializer_class = school_serializer
    # serializer = school_serializer
