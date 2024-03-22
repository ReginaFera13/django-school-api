from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.db.models import Avg
from .models import Subject
from grade_app.models import Grade

class SubjectSerializer(ModelSerializer):
    students = SerializerMethodField()
    grade_average = SerializerMethodField()
    
    class Meta:
        model = Subject
        fields = ['subject_name', 'professor', 'students', 'grade_average']
    
    def get_students(self, instance):
        students = instance.students.count()
        return students
    
    def get_grade_average(self, instance):
        related_grades = Grade.objects.filter(a_subject=instance)
        grade_average = related_grades.aggregate(avg_grade=Avg('grade'))['avg_grade']
        if grade_average is not None:
            # Round to the nearest two decimals
            return round(grade_average, 2)
        else:
            return 0 
