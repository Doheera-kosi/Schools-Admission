from django.shortcuts import render #type: ignore

from rest_framework import viewsets #type: ignore
from .models import Class
from .serializers import ClassSerializer
from rest_framework.response import Response  #type:ignore

# Create your views here.

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class SchoolClassesViewSet(viewsets.ViewSet):
    """
    A custom viewset to retrieve classes belonging to a specific school.
    """

    def list(self, request, pk=None):
        queryset = Class.objects.filter(school_id=pk)
        serializer = ClassSerializer(queryset, many=True)
        return Response(serializer.data)