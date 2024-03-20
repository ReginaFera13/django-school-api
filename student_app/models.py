from django.db import models
from django.core import validators as v
from .validators import validate_name, validate_school_email, validate_combination

# Create your models here.

class Student(models.Model):
    name = models.CharField(unique=False, validators=[v.MaxLengthValidator(50), validate_name])
    student_email = models.EmailField(unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(unique=True)
    locker_number = models.IntegerField(default=110, unique=True, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(default='12-12-12', unique=False, validators=[v.MaxLengthValidator(8), validate_combination])
    good_student = models.BooleanField(default=True, unique=False)
    
    def __str__(self):
        return f'{self.name} - {self.student_email} - {self.locker_number}'
    
    def locker_reassignment(self, new_locker):
        self.locker_number = new_locker
        self.save()
        
    def student_status(self):
        self.good_student = not self.good_student
        self.save()
        
    
