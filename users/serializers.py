from django.contrib.auth import get_user_model
from rest_framework import serializers, settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from main.models import Company

CustomUser = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class CustomUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "name",
            "role",
        )


class CustomUserWriteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "name",
            "email",
            "role",
            "password",
        )

    def create(self, validated_data):
        custom_user = CustomUser.objects.create_user(**validated_data)
        if custom_user.role == CustomUser.Role.COMPANY:
            Company.objects.create(owner=custom_user,name=custom_user.name)
        return custom_user






class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        tokens = super().validate(attrs)
        attrs = CustomUserReadSerializer(instance=self.user).data
        attrs.update(dict(tokens=tokens))
        return attrs
