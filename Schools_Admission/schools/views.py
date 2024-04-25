from django.shortcuts import render #type: ignore

# Create your views here.
from rest_framework import viewsets, generics, status #type: ignore
from .models import School
from .serializers import SchoolSerializer #type: ignore
from students.models import Student
from students.serializers import StudentSerializer
from rest_framework.response import Response        #type: ignore


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    

class SchoolStudentsDetailView(generics.RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Retrieve all admitted students for the current school
        admitted_students = Student.objects.filter(school=instance.id)
        student_serializer = StudentSerializer(admitted_students, many=True)

        # Construct the response data
        response_data = {
            'school_details': serializer.data,
            'admitted_students': student_serializer.data
        }

        return Response(response_data, status=status.HTTP_200_OK)