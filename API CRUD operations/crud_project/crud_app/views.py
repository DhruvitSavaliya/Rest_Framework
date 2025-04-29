from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer
from django.shortcuts import get_object_or_404

class DoctorList(APIView):
     def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

class DoctorCreate(APIView):
     def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorDetail(APIView):
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, id=pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, id=pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, id=pk)
        doctor.delete()
        return Response({"message": "Doctor deleted successfully."}, status=status.HTTP_204_NO_CONTENT)