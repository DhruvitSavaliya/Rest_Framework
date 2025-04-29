from django.shortcuts import render
from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>Welcome to the API Project! </h1><p>Go to <a href='/doctors/'>Doctors API</a></p>")


class DoctorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
