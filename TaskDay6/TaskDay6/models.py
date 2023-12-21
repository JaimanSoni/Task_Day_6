# models.py
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    admission_date = models.DateField()
    program_of_study = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.student_id}"
