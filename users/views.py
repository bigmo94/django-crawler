from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .forms import LoginForm, ProfileForm, ConfigurationCodeForm
from django.views import generic
from .models import Profile
from .permission import IsUserOwnerOrJustRead, IsUserAdmin
from .serializer import UserSerializer
import random
from django.core.cache import cache

User = get_user_model()


def generate_code():
    return random.randint(10000, 99999)


def registration(request):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        form2 = ProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid() and form2.is_valid():
            cd1 = form.cleaned_data
            cd2 = form2.cleaned_data
            code = generate_code()
            cache.set('username', cd1.get('username'), timeout=30)
            cache.set('password', cd1.get('password'), timeout=30)
            cache.set("first_name", cd1.get('first_name'), timeout=30)
            cache.set("last_name", cd1.get('last_name'), timeout=30)
            cache.set("email", cd1.get('email'), timeout=30)
            cache.set("phone_number", cd2.get('phone_number'), timeout=30)
            cache.set("age", cd2.get('age'), timeout=30)
            cache.set("bio", cd2.get('bio'), timeout=30)
            cache.set("avatar", cd2.get('avatar'), timeout=30)
            cache.set('code', code, timeout=30)
            print(code)
            activation_form = ConfigurationCodeForm()
            return render(request, 'users/confirm_code.html', {'form': activation_form})
    else:
        form2 = ProfileForm()
    return render(request, 'users/register.html', {'form': form, 'form2': form2})


def confirm_registration(request):
    form = ConfigurationCodeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            code = form.cleaned_data['code']
            cache_code = cache.get('code')
            if not cache_code == code:
                return redirect('users:register')
            username = cache.get('username')
            password = cache.get('password')
            email = cache.get('email')
            first_name = cache.get('first_name')
            last_name = cache.get('last_name')
            phone_number = cache.get('phone_number')
            age = cache.get('age')
            bio = cache.get('bio')
            avatar = cache.get('avatar')
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                            last_name=last_name)
            profile = Profile.objects.create(user=user, phone_number=phone_number, age=age, avatar=avatar, bio=bio)
            profile.save()
            login(request, user)
            return redirect('users:profile_detail')


class LoginUser(generic.View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        context = {'form': form}
        return render(self.request, "users/login.html", context)

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(self.request, user)
                return redirect(f'/account/profile-detail/{user.id}/')
            return self.get(self.request)


class ProfileDetailView(generic.DetailView):
    template_name = 'users/profile_detail.html'
    model = Profile
    context_object_name = 'profile'

    def get_object(self):
        return Profile.objects.get(user_id=self.kwargs['profile_id'])


class LogoutUser(generic.View):
    def get(self, request):
        logout(request)
        return render(request, 'users/logout.html')


class UserListAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsUserOwnerOrJustRead,)
    authentication_classes = (TokenAuthentication,)


class UserRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsUserAdmin,)
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
