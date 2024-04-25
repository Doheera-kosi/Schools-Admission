from django.shortcuts import render   #type: ignore

from rest_framework import viewsets   #type: ignore
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
