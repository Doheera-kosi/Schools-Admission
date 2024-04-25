from django.shortcuts import render   #type: ignore

# Create your views here.
from rest_framework import viewsets #type: ignore
from .models import Course
from .serializers import CourseSerializer #type: ignore

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    