from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(_('age'))
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='avatars')
    phone_number = models.PositiveBigIntegerField(_('phone number'), unique=True)
    bio = models.TextField(_('bio'), blank=True)

    class Meta:
        db_table = 'profiles'
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return '{}'.format(self.user)

