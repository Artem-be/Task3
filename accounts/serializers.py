from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, RefreshToken
from django.utils import timezone

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.UUIDField(required=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': False}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(required=True)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        token = self.get_token(user)

        refresh_token = RefreshToken.objects.create(user=user, expires_at=timezone.now() + timezone.timedelta(days=30))

        return {
            'access_token': str(token.access_token),
            'refresh_token': str(refresh_token.token),
        }