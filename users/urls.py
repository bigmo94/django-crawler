from django.urls import path
from .views import (LoginUser,
                    ProfileDetailView,
                    LogoutUser,
                    UserLoginAPIView,
                    UserListAPIView,
                    confirm_registration,
                    UserRetrieveDestroyAPIView,
                    UserRegisterAPIView,
                    UserConfirmAPIView)

app_name = 'users'
urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('login-api/', UserLoginAPIView.as_view(), name='login-step1'),
    path('profile-detail/<int:profile_id>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('register/step-1/', UserRegisterAPIView.as_view(), name='register-step1'),
    path('register/step-2/', UserConfirmAPIView.as_view(), name='register-step2'),
    path('user-api/', UserListAPIView.as_view(), name='user_api'),
    path('confirm-register/', confirm_registration, name='confirm'),
    path('user-api/<int:pk>/', UserRetrieveDestroyAPIView.as_view(), name='user-detail'),
]
