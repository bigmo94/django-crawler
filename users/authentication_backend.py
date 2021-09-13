from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, BaseBackend
from django.db.models import Q
from django.core.cache import cache

User = get_user_model()


class UserAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return
        user = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if user is None:
            return
        if user.check_password(password):
            return user


class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        if not email or not password:
            return

        cache_key = 'login_code_{}'.format(email)
        verify_code = cache.get(cache_key)

        if verify_code != password:
            return

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        return user
