from django.db import models
from django.core import validators as v
from .validators import validate_name, validate_school_email, validate_combination
from subject_app.models import Subject

# Create your models here.

class Student(models.Model):
    name = models.CharField(unique=False, validators=[v.MaxLengthValidator(50), validate_name])
    student_email = models.EmailField(unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(unique=True)
    locker_number = models.IntegerField(default=110, unique=True, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(default='12-12-12', unique=False, validators=[v.MaxLengthValidator(8), validate_combination])
    good_student = models.BooleanField(default=True, unique=False)
    subjects = models.ManyToManyField(Subject, related_name='students')
    
    def __str__(self):
        return f'{self.name} - {self.student_email} - {self.locker_number}'
    
    def locker_reassignment(self, new_locker):
        self.locker_number = new_locker
        self.save()
        
    def student_status(self):
        self.good_student = not self.good_student
        self.save()
        
    def add_subject(self, subject_id):
        if self.subjects.count() < 8:
            self.subjects.add(subject_id)
            return self.subjects
        else:
            raise Exception('This students class schedule is full!')
    
    def remove_subject(self, subject_id):
        if self.subjects.count() > 0:
            self.subjects.remove(subject_id)
            return self.subjects
        else:
            raise Exception('This students class schedule is empty!')