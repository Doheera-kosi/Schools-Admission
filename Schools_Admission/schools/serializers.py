from rest_framework import serializers #type: ignore
from .models import School
from courses.serializers import CourseSerializer

class SchoolSerializer(serializers.ModelSerializer):
    # courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = '__all__'
        # fields = ['id', 'name', 'location']
