from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, CustomTokenObtainPairSerializer, LogoutSerializer
from .models import RefreshToken, User
from django.utils import timezone


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class MeView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class RefreshTokenView(generics.GenericAPIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        try:
            token = RefreshToken.objects.get(token=refresh_token)

            if token.expires_at < timezone.now():
                return Response({"error": "Refresh token has expired."}, status=status.HTTP_400_BAD_REQUEST)

            user = token.user
            access_token = self.create_access_token(user)

            token.expires_at = timezone.now() + timezone.timedelta(days=30)
            token.save()

            return Response({
                'access_token': access_token,
                'refresh_token': str(token.token)
            })
        except RefreshToken.DoesNotExist:
            return Response({"error": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)

    def create_access_token(self, user):
        token = CustomTokenObtainPairSerializer.get_token(user)
        return str(token.access_token)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data['refresh_token']
        try:
            token = RefreshToken.objects.get(token=refresh_token)
            token.delete()
            return Response({"success": "User  logged out."}, status=status.HTTP_200_OK)
        except RefreshToken.DoesNotExist:
            return Response({"error": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)
