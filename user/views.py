from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status, serializers
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from user.models import CustomUser
from user.serializers import CustomTokenObtainPairSerializer, UserSerializer


# Create your views here.
class CreateUser(CreateAPIView):
    model = CustomUser
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'Response': "User is Successfully Created"}, status=status.HTTP_201_CREATED, headers=headers)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
