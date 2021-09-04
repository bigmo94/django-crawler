from django.urls import path
from .views import LoginUser, ProfileDetailView, LogoutUser

app_name = 'users'
urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('profile-detail/<int:profile_id>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('logout/', LogoutUser.as_view(), name='logout'),
]
