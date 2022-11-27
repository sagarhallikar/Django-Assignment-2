
from rest_framework import serializers
from rest_framework import generics
from .models import *
from .serializers import EmployeeSerializer
# Create your views here.




from django.shortcuts import render



class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee
    serializer_class = EmployeeSerializer
