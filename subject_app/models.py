from django.db import models
from django.core import validators as v
from .validators import validate_subject_format, validate_professor_name

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(unique=True, validators=[validate_subject_format])
    professor = models.CharField(unique=False, validators=[validate_professor_name])
    # students = models.ManyToManyField(Student, related_name='subjects', validators=[v.MinLengthValidator(0), v.MaxLengthValidator(31)])
    
    def __str__(self):
        return f'{self.subject_name} - {self.professor} - {len(self.students)}'
    
    def add_a_student(self, student_id):
        if self.students.count() < 31:
            self.students.add(student_id)
            return self.students
        else:
            raise Exception('This subject is full!')
    
    def drop_a_student(self, student_id):
        if self.students.count() > 0:
            self.students.remove(student_id)
            return self.students
        else:
            raise Exception('This subject is empty!')