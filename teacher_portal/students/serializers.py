from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'subject', 'mark']
        read_only_fields = ['id', 'created_at', 'updated_at']
