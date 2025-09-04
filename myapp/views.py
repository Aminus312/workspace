from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Staff
from .forms import StudentRegistrationForm, StaffRegistrationForm

def landing_page(request):
    """Landing page view with system statistics"""
    # Calculate statistics for the system overview
    total_students = Student.objects.count()
    total_staff = Staff.objects.count()
    
    # Calculate unique departments from students and designations from staff
    student_departments = set(Student.objects.values_list('department', flat=True))
    staff_designations = set(Staff.objects.values_list('designation', flat=True))
    # Combine both for total unique departments/designations
    total_departments = len(student_departments.union(staff_designations))
    
    context = {
        'total_students': total_students,
        'total_staff': total_staff,
        'total_departments': total_departments,
    }
    
    return render(request, 'landing.html', context)

def student_registration(request):
    """Student registration view"""
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student registered successfully!')
            return redirect('student_registration')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'student_registration.html', {'form': form})

def students_record(request):
    """Students record view"""
    students = Student.objects.all()
    return render(request, 'students_record.html', {'students': students})

def add_staff(request):
    """Add staff view"""
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff member added successfully!')
            return redirect('add_staff')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StaffRegistrationForm()
    
    return render(request, 'add_staff.html', {'form': form})

def staff_records(request):
    """Staff records view"""
    staff_members = Staff.objects.all()
    return render(request, 'staff_records.html', {'staff_members': staff_members})

def contact_us(request):
    """Contact us view"""
    return render(request, 'contact_us.html')