from django.contrib import admin
from .models import Student, Staff

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'course', 'department', 'school', 'created_at']
    list_filter = ['department', 'school', 'course', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'course']
    ordering = ['-created_at']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'staff_id', 'designation', 'created_at']
    list_filter = ['designation', 'created_at']
    search_fields = ['full_name', 'email', 'staff_id']
    ordering = ['-created_at']