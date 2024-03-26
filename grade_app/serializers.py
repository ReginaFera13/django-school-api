from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Grade, Student, Subject


class GradeSerializer(ModelSerializer):
    students = SerializerMethodField()
    grade_average = SerializerMethodField()
    
    class Meta:
        model = Grade
        fields = '__all__'