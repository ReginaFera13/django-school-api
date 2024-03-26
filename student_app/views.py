from django.shortcuts import render, get_object_or_404
from .serializers import StudentAllSerializer, Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK

# Create your views here.
class All_students(APIView):
    def get(self, request):
        students = StudentAllSerializer(Student.objects.all(), many=True)
        return Response(students.data)
    
    def post(self, request):
        serializer = StudentAllSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class A_students(APIView):
    def get(self, request, id):
        student = get_object_or_404(Student, id = id)
        return Response(StudentAllSerializer(student).data)
    
    def put(self, request, id, subject_id):
        student = get_object_or_404(Student, id = id)
        student.add_subject(subject_id)
        ser_student = StudentAllSerializer(student, data = vars(student))
        ser_student = StudentAllSerializer(student, data = request.data, partial = True)
        if ser_student.is_valid():
            ser_student.save()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(ser_student.errors, status=HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        student = get_object_or_404(Student, id = id)
        if 'locker_number' in request.data and request.data['locker_number']:
            student.locker_reassignment()
        if 'good_student' in request.data and request.data['good_student']:
            student.student_status()
        if 'subjects' in request.data:
            student.remove_subject()
        ser_student = StudentAllSerializer(student, data = request.data, partial = True)
        if ser_student.is_valid():
            ser_student.save()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(ser_student.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        student = get_object_or_404(Student, id = id)
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)