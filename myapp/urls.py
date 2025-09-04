from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register-student/', views.student_registration, name='student_registration'),
    path('students-record/', views.students_record, name='students_record'),
    path('add-staff/', views.add_staff, name='add_staff'),
    path('staff-records/', views.staff_records, name='staff_records'),
    path('contact-us/', views.contact_us, name='contact_us'),
]