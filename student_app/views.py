from django.shortcuts import render
from .serializers import StudentAllSerializer, Student
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class All_students(APIView):
    def get(self, request):
        students = StudentAllSerializer(Student.objects.all(), many=True)
        return Response(students.data)