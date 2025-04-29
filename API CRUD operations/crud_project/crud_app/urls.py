from django.urls import path
from .views import DoctorDetail,DoctorCreate,DoctorList

urlpatterns = [
    path('Doctors/',DoctorList.as_view(),name='doctor-list'),
    path('Doctors/create/',DoctorCreate.as_view(),name='doctor-create'),
    path('Doctors/<int:pk>/',DoctorDetail.as_view(),name="doctor-details"),
]