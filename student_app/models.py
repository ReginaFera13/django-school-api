from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, unique=False)
    student_email = models.EmailField(max_length=50, unique=True)
    personal_email = models.EmailField(max_length=50, unique=True)
    locker_number = models.IntegerField(default=110, unique=True)
    locker_combination = models.CharField(max_length=50, default='12-12-12', unique=False)
    good_student = models.BooleanField(default=True, unique=False)
    
    def __str__(self):
        return f'{self.name} - {self.student_email} - {self.locker_number}'
    
    def locker_reassignment(self, new_locker):
        self.locker_number = new_locker
        self.save()
        
    def student_status(self):
        self.good_student = not self.good_student
        self.save()
        
    
