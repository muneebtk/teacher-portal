from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
        )

    def create(self, validated_data):
        if validated_data.get("password") != validated_data.get("confirm_password"):
            raise serializers.ValidationError("Passwords do not match")
        if User.objects.filter(email=validated_data["email"]).exists():
            raise serializers.ValidationError("Email already exists")

        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "is_staff", "is_active")
        read_only_fields = ("id", "email", "first_name", "last_name", "is_staff", "is_active")
