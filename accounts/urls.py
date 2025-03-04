from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, RefreshTokenView, LogoutView, MeView, APIRootView

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', RefreshTokenView.as_view(), name='refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', MeView.as_view(), name='me'),
]
