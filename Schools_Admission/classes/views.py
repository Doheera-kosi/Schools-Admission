from django.shortcuts import render #type: ignore

from rest_framework import viewsets, status #type: ignore
from .models import Class
from .serializers import ClassSerializer
from rest_framework.response import Response  #type:ignore

# Create your views here.

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    
    def enroll_student(self, request, pk=None):
        try:
            class_instance = self.get_object()
            if class_instance.enroll_student():
                return Response({'message': 'Student enrolled successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Class is already full'}, status=status.HTTP_400_BAD_REQUEST)
        except Class.DoesNotExist:
            return Response({'message': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)


class SchoolClassesViewSet(viewsets.ViewSet):
    """
    A custom viewset to retrieve classes belonging to a specific school.
    """

    def list(self, request, pk=None):
        queryset = Class.objects.filter(school_id=pk)
        serializer = ClassSerializer(queryset, many=True)
        return Response(serializer.data)