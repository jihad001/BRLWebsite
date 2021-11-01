from django.db import models
from django.db.models import fields
from rest_framework import serializers
from accounts.models import UserExtension, Teacher, Student
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']



class UserExtensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExtension
        fields = ['id', 'nick_name', 'phone_number', 'date_of_birth', 'type', 'department', 'university', 'educational_background', 'address',]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_id', 'student_type', 'session',]
        
        

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'designation', 'teacher_type',]
        
        
        
        
        
class UserDetailedSerializer(serializers.ModelSerializer):
    user_extension = UserExtensionSerializer()
    student_data = StudentSerializer()
    teacher_data = TeacherSerializer()
    
    class Meta:
        model = User
        fields = ['id', 
                  'username', 
                  'first_name', 
                  'last_name', 
                  'email', 
                  'user_extension', 
                  'student_data', 
                  'teacher_data',
                  ]