from rest_framework import serializers
from .models import Student, School


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student', 'roll', 'school']


class SchoolSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = School
        fields = ['school', 'student']