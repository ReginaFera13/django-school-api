from django.shortcuts import render, get_object_or_404
from .serializers import GradeSerializer, Grade, Student, Subject
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK

# Create your views here.
class All_grades(APIView):
    def get(self, request):
        grades = GradeSerializer(Grade.objects.all(), many=True)
        return Response(grades.data)
    
    def post(self, request, student, subject):
        student = get_object_or_404(Student, name = student)
        subject = get_object_or_404(Subject, subject_name = subject)
        grade_data = {'grade': 100.00, 'student': student.id, 'a_subject': subject.id}
        serializer = GradeSerializer(data=grade_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class A_grades(APIView):
    
    def get_grade(self, student, subject):
        student = get_object_or_404(Student, name = student)
        subject = get_object_or_404(Subject, subject_name = subject)
        grade = Grade.objects.filter(student=student, subject=subject)
        return grade
        
    def get(self, request, student, subject):
        grade = self.get_grade(student, subject)
        return Response(GradeSerializer(grade).data) 
    
    def put(self, request, student, subject):
        grade = self.get_grade(student, subject)
        new_grade_value = request.data.get('grade')
        if new_grade_value is not None:
            grade.grade = new_grade_value
            grade.save()
            return Response(GradeSerializer(grade).data, status=HTTP_200_OK)
        return Response({'error': 'Grade value is required'}, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, student, subject):
        grade = self.get_grade(student, subject)
        grade.delete()
        return Response(status=HTTP_204_NO_CONTENT)