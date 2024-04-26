from django.shortcuts import render #type: ignore

# Create your views here.
from rest_framework import viewsets, generics, status #type: ignore
from .models import School
from .serializers import SchoolSerializer #type: ignore
from students.models import Student
from students.serializers import StudentSerializer
from courses.serializers import CourseSerializer
from courses.models import Course
from rest_framework.decorators import action        #type: ignore

from rest_framework.response import Response        #type: ignore


# class SchoolViewSet(viewsets.ModelViewSet):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
    
    
#     @action(detail=True, methods=['get'])
#     def courses(self, request, pk=None):
#         name = self.get_object()
#         courses = School.objects.filter(name=name)
#         serializer = SchoolSerializer(courses, many=True)
#         return Response(serializer.data)

#     @action(detail=True, methods=['get'])
#     def course_count(self, request, pk=None):
#         name = self.get_object()
#         course_count = School.objects.filter(name=name).count()
#         return Response({'course_count': course_count})


# **************************************************************
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        school = self.get_object()
        courses = school.courses.all()  # Retrieve all courses associated with the school
        course_list = [course.name for course in courses]  # Extract the names of the courses
        return Response({'courses': course_list})

    @action(detail=True, methods=['get'])
    def course_count(self, request, pk=None):
        school = self.get_object()
        course_count = school.courses.count()  # Count the number of courses associated with the school
        return Response({'course_count': course_count})
    
    # method that checks the school's full capacity:
    def school_full_status(self, request, pk=None):
        try:
            school_instance = self.get_object()
            if school_instance.is_full():
                return Response({'message': 'The school is full'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'The school is not full'}, status=status.HTTP_200_OK)
        except School.DoesNotExist:
            return Response({'message': 'School not found'}, status=status.HTTP_404_NOT_FOUND)

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