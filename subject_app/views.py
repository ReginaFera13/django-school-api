from django.shortcuts import render, get_object_or_404
from .serializers import SubjectSerializer, Subject
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK

# Create your views here.
class All_subjects(APIView):
    def get(self, request):
        subjects = SubjectSerializer(Subject.objects.all(), many=True)
        return Response(subjects.data)
    
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        

class A_subjects(APIView):
    def get(self, request, subject):
        subject = get_object_or_404(Subject, subject_name = subject.title())
        return Response(SubjectSerializer(subject).data)
    
    def put(self, request, subject):
        subject = get_object_or_404(Subject, subject_name = subject.title())
        if 'professor' in request.data and request.data['professor']:
            subject.professor = request.data.get('professor')
        if 'subject_name' in request.data and request.data['subject_name']:
            subject.subject_name = request.data.get('subject_name')
        ser_subject = SubjectSerializer(subject, data = request.data, partial = True)
        if ser_subject.is_valid():
            ser_subject.save()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(ser_subject.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, subject):
        subject = get_object_or_404(Subject, subject_name = subject.title())
        subject.delete()
        return Response(status=HTTP_204_NO_CONTENT)