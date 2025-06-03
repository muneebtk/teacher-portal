from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer, UserDetailSerializer
from .models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """user registration view, handles user registration"""
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "user": UserDetailSerializer(user).data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            # Handle validation errors
            error_messages = [
                f"{field}: {error}"
                for field, errors in serializer.errors.items()
                for error in (errors if isinstance(errors, list) else [errors])
            ]
        return Response({"errors": error_messages}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """Render the registration page"""
        return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'redirect_url': '/students/students/'})
        else:
            return JsonResponse({'status': 'fail', 'message': 'Invalid credentials'})
    return render(request, 'signin.html')


class UserLogoutView(APIView):
    def get(self, request):
        """user logout view"""
        logout(request)

        return redirect('/accounts/signin/')