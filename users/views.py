from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView

from . import serializers

from django.http import HttpResponse
from rest_framework.decorators import api_view
from .task import mod


CustomUser = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = serializers.CustomUserWriteSerializer


class LoginView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer


@api_view(['GET'])
def get_test_add(request):
    x, y = int(request.query_params.get('x')), int(request.query_params.get('y'))
    mod.apply_async(args=(x, y), countdown=20)
    return HttpResponse(f'Success !')
