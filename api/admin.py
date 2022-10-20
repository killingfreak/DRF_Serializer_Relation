from django.contrib import admin
from .models import Student,School
# Register your models here.

@admin.register(School)
class School(admin.ModelAdmin):
    list_display = [id,'school']

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display = ['roll', 'student', 'school']
