# serializers.py

from rest_framework import serializers
from .models import User, Department, Student, Course, AttendanceLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'type', 'full_name', 'username', 'email'] 

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer() # Nest User data
    department = DepartmentSerializer()

    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer() 

    class Meta:
        model = Course
        fields = '__all__'

class AttendanceLogSerializer(serializers.ModelSerializer):
    student = StudentSerializer() 
    course = CourseSerializer() 

    class Meta:
        model = AttendanceLog
        fields = '__all__' 
