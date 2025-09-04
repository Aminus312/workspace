from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    home_address = models.TextField()
    password = models.CharField(max_length=128)
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-created_at']

class Staff(models.Model):
    DESIGNATION_CHOICES = [
        ('Business Manager', 'Business Manager'),
        ('Human Resource Manager', 'Human Resource Manager'),
        ('Lecturer', 'Lecturer'),
        ('Software Engineer', 'Software Engineer'),
        ('Programmer', 'Programmer'),
        ('Business Analyst', 'Business Analyst'),
    ]
    
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    staff_id = models.CharField(max_length=50, unique=True)
    home_address = models.TextField()
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.designation}"

    class Meta:
        ordering = ['-created_at']