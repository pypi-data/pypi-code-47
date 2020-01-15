from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model

User = get_user_model()


class CriadoEditadoMixin(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)
    #criado_por = models.ForeignKey(User, related_name='criador_de', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    class Meta:
        abstract = True
