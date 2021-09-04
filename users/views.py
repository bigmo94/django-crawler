from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.views import generic
from .models import Profile


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
