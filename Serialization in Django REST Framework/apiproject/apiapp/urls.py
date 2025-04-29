from django.urls import path
from .views import home,DoctorListCreateAPIView, DoctorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('',home, name='home'),
    path('doctors/', DoctorListCreateAPIView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyAPIView.as_view(), name='doctor-detail'),
]
