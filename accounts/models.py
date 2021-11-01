from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class UserExtension(models.Model):
    USER_TYPES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('staff', 'Staff'),
    ]
    
    nick_name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    user = models.OneToOneField(User, on_delete=CASCADE, related_name='user_extension')
    date_of_birth = models.DateField(null=True)
    type = models.CharField(max_length=15, choices=USER_TYPES, default='student')
    regestered = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    department = models.CharField(max_length=255, default='Applied Chemistry and Chemcal Engineering')
    university = models.CharField(max_length=255, default='University of Chittagong')
    educational_background = models.TextField(null=True)
    address = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'Users Extension'


    def __str__(self):
        return self.user.username
    
    

class Student(models.Model):
    STUDENT_TYPES = [
        ('thesis', 'Thesis'),
        ('senior', 'Senior'),
        ('nondegree', 'Non Degree'),
    ]
    
    student_id = models.CharField(max_length=15, null=True)
    student_type = models.CharField(max_length=15, choices=STUDENT_TYPES, default='nondegree')
    session = models.CharField(max_length=15, null=True)
    is_current = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=CASCADE, related_name='student_data')
    
    def __str__(self):
        return self.user.username
    
    

class Teacher(models.Model):
    TEACHER_TYPE = [
        ('principal', 'Principal Investigator'),
        ('regular', 'Regular Supervisor')
    ]
    
    designation = models.CharField(max_length=100, null=True)
    user = models.OneToOneField(User, on_delete=CASCADE, related_name='teacher_data')
    teacher_type = models.CharField(max_length=50, choices=TEACHER_TYPE, default='regular')
    
    
    def __str__(self):
        return self.user.username
    
