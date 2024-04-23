from django.shortcuts import render #type: ignore

# Create your views here.
from rest_framework import viewsets #type: ignore
from .models import School
from .serializers import SchoolSerializer #type: ignore

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    

