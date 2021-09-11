from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, ProfileForm
from django.views import generic
from .models import Profile


def registration(request):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        form2 = ProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid() and form2.is_valid():
            user = form.save(commit=False)
            first_name = form2.cleaned_data.get('first_name')
            last_name = form2.cleaned_data.get('last_name')
            email = form2.cleaned_data.get('email')
            bio = form2.cleaned_data.get('bio')
            avatar = form2.cleaned_data.get('avatar')
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            age = form2.cleaned_data.get('age')
            phone_number = form2.cleaned_data.get('phone_number')
            user.save()
            Profile(user=user, age=age, phone_number=phone_number, avatar=avatar, bio=bio).save()
            login(request, user)
            return redirect('users:login')
    form2 = ProfileForm()
    context = {'form': form,
               'form2': form2}
    return render(request, 'users/register.html', context)


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
