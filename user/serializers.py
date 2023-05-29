# users/serializers.py

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        if email:
            try:
                CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError({"message": "invalid email."})
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)

        data.update({
            'username': self.user.username,
            'email': self.user.email,
            'user_id': self.user.id
        })
        return data
