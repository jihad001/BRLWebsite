from django.contrib import admin
from .models import UserExtension, Student, Teacher


admin.site.register(UserExtension)
admin.site.register(Student)
admin.site.register(Teacher)