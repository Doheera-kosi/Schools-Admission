from rest_framework import serializers #type: ignore
from .models import School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        # fields = ['id', 'name', 'location']
