from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from utils.models import UUIDMixin
from .managers import UserManager
from .validators import validate_cpf


class Usuario(UUIDMixin, AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(_('CPF'), max_length=11, unique=True, validators=[validate_cpf])
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(_('full name'), max_length=60)  
    nick_name = models.CharField(_('nick name'), max_length=30)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['email', 'full_name', 'nick_name']

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
    
    def get_full_name(self):          
        return self.full_name

    def get_short_name(self):        
        return self.nick_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)