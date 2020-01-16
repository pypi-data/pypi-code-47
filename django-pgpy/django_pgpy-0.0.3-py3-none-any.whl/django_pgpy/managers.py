from django.db import models

from django_pgpy.helpers import create_identity
from django_pgpy import settings


class UserIdentityManager(models.Manager):
    def create(self, user, password, restorers=None, name=None):
        if restorers is None:
            restorers = settings.DJANGO_PGPY_DEFAULT_RESTORERS(user)

        public_keys = [r.public_key for r in restorers]
        key, hash_info, secret_blob = create_identity(user.username if user else name,
                                                      user.email if user else None,
                                                      password,
                                                      public_keys)

        instance = super().create(user=user,
                                  public_key_blob=str(key.pubkey),
                                  private_key_blob=str(key),
                                  secret_blob=str(secret_blob) if secret_blob else None,
                                  hash_info=hash_info)

        for r in restorers:
            instance.encrypters.add(r)

        return instance

    def exists_for_user(self, user):
        return self.filter(user=user).exists()


class EncryptedMessageManager(models.Manager):
    def create(self, text, encrypters, **kwargs):
        instance = self.model(**kwargs)
        instance.encrypt(text, encrypters)

        return instance
