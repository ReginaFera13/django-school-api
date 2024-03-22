from rest_framework.serializers import ModelSerializer, SerializerMethodField
from subject_app.serializers import SubjectSerializer
from .models import Student

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'locker_number']

class StudentAllSerializer(ModelSerializer):
    subjects = SerializerMethodField()
    
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'personal_email', 'locker_number', 'locker_combination', 'good_student', 'subjects']
    
    def get_subjects(self, instance):
        subjects = instance.subjects.all()
        ser_subjects = SubjectSerializer(subjects, many=True).data
        return ser_subjects