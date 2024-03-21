from django.shortcuts import render
from .serializers import studentsserializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import students

# Create your views here.
class StudentListCreateAPIView(ListCreateAPIView):
    queryset = students.objects.all()
    serializer_class=studentsserializer

class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = students.objects.all()
    serializer_class = studentsserializer

