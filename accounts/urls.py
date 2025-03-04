from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, RefreshTokenView, LogoutView, MeView, APIRootView

urlpatterns = [
<<<<<<< HEAD
    path('', APIRootView.as_view(), name='api-root'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', RefreshTokenView.as_view(), name='refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', MeView.as_view(), name='me'),
=======
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', views.RefreshTokenView.as_view(), name='refresh'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('me/', views.MeView.as_view(), name='me'),
>>>>>>> 7de88bb45d4472fc555fe726726153789a9b37e3
]
