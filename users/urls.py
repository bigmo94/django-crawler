from django.urls import path
from .views import (LoginUser,
                    ProfileDetailView,
                    LogoutUser,
                    registration,
                    UserListAPIView,
                    confirm_registration,
                    UserRetrieveDestroyAPIView)

app_name = 'users'
urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('profile-detail/<int:profile_id>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('register/', registration, name='register'),
    path('user-api/', UserListAPIView.as_view(), name='user_api'),
    path('confirm-register/', confirm_registration, name='confirm'),
    path('user-api/<int:pk>/', UserRetrieveDestroyAPIView.as_view(), name='user-detail'),
]
