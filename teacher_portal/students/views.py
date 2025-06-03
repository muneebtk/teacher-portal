import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from django.contrib.auth.decorators import login_required
from django.db.models import F


@login_required(login_url='/accounts/signin/')
@ensure_csrf_cookie
def students_view(request):
    """Handle both HTML template and JSON API for students"""
    user = request.user
    
    if request.method == 'GET':
        students = Student.objects.filter(teacher=user)
        
        if request.headers.get('Accept') == 'application/json':
            serializer = StudentSerializer(students, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            # Return HTML template for direct page visits
            serializer = StudentSerializer(students, many=True)
            return render(request, 'dashboard.html', {
                'students': serializer.data,
                'user': user
            })
    
    elif request.method == 'POST':
        # Create new student or update existing one
        try:
            data = json.loads(request.body)
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                # Attempt to update the record
                updated_count = Student.objects.filter(
                    name=serializer.validated_data['name'],
                    subject=serializer.validated_data['subject'],
                    teacher=user
                ).update(
                    mark=F('mark') + serializer.validated_data['mark']
                )

                # If no record was updated, create a new one
                if updated_count == 0:
                    Student.objects.create(
                        name=serializer.validated_data['name'],
                        subject=serializer.validated_data['subject'],
                        mark=serializer.validated_data['mark'],
                        teacher=user
                    )
                return JsonResponse({
                    'student': serializer.data,
                    'message': 'Student created successfully'
                }, status=201)
            else:
                return JsonResponse({
                    'errors': serializer.errors
                }, status=400)
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON data'
            }, status=400)


@login_required(login_url='/accounts/signin/')
@require_http_methods(["GET", "PUT", "DELETE"])
def student_detail_view(request, pk):
    """Handle individual student operations"""
    user = request.user
    student = get_object_or_404(Student, pk=pk, teacher=user)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            serializer = StudentSerializer(student, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({
                    'student': serializer.data,
                    'message': 'Student updated successfully'
                })
            else:
                return JsonResponse({
                    'errors': serializer.errors
                }, status=400)
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON data'
            }, status=400)
    
    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({
            'message': 'Student deleted successfully'
        }, status=204)
