# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import students_view, student_detail_view

urlpatterns = [
    
    path('students/', students_view, name='students-api'),
    path('students/<int:pk>/', student_detail_view, name='student-detail'),
]
