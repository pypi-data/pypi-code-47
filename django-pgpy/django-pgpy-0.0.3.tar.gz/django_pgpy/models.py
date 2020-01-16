from __future__ import unicode_literals, annotations

import warnings
from contextlib import nullcontext
from typing import List, Union

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE, QuerySet
from django.utils import timezone
from django.utils.functional import cached_property
from pgpy import PGPKey, PGPMessage
from pgpy.errors import PGPError

from django_pgpy.helpers import hash_password, encrypt_private_key_by_password, create_session_key, encrypt, add_encrypters
from django_pgpy.managers import EncryptedMessageManager, UserIdentityManager


def get_secret(decrypter_uid: Identity, secret_blob: str) -> str:
    assert decrypter_uid.private_key.is_unlocked

    encrypted_message = PGPMessage.from_blob(secret_blob)
    msg = decrypter_uid.private_key.decrypt(encrypted_message)
    return msg.message


class Identity(models.Model):
    objects = UserIdentityManager()

    user = models.OneToOneField(get_user_model(),
                                on_delete=CASCADE,
                                null=True,
                                blank=True,
                                related_name='pgp_identity')

    encrypters = models.ManyToManyField(
        'self',
        related_name='restorable_identities',
        symmetrical=False,
    )

    public_key_blob = models.TextField()
    private_key_blob = models.TextField()
    secret_blob = models.TextField(null=True, blank=True)
    hash_info = models.CharField(max_length=256, null=True, blank=True)

    @cached_property
    def public_key(self) -> PGPKey:
        key, _ = PGPKey.from_blob(self.public_key_blob)
        return key.pubkey

    @cached_property
    def private_key(self) -> PGPKey:
        key, _ = PGPKey.from_blob(self.private_key_blob)
        return key

    def get_secret(self, decrypter_uid: Identity) -> str:
        return get_secret(decrypter_uid, self.secret_blob)

    def set_secret(self, secret):
        cipher, sessionkey = create_session_key()

        msg = PGPMessage.new(secret)
        for r in self.encrypters.all():
            msg = r.public_key.encrypt(msg, cipher=cipher, sessionkey=sessionkey)

        msg = self.public_key.encrypt(msg, cipher=cipher, sessionkey=sessionkey)

        del sessionkey
        self.secret_blob = str(msg)

    @property
    def can_decrypt(self):
        return self.reset_requests.filter(secret_blob__isnull=False).exists() is False

    def protect(self, password):
        self.hash_info, password_hash = hash_password(password)
        encrypt_private_key_by_password(self.private_key, password_hash)
        return password_hash

    def unlock(self, password):
        _, password_hash = hash_password(password, self.hash_info)
        return self.private_key.unlock(password_hash)

    def decrypt(self, encrypted_msg, password=None):
        unlock_gen = self.unlock(password) if password else nullcontext()

        with unlock_gen:
            return encrypted_msg.decrypt(self)

    def change_password(self, old_password: str, new_password: str):

        with self.unlock(old_password):
            new_password_hash = self.protect(new_password)

            self.private_key_blob = str(self.private_key)
            self.set_secret(new_password_hash)

            self.save()

    def reset_password(self, new_pwd):
        hash_info, new_secret = hash_password(new_pwd)
        public_keys = [e.public_key for e in self.encrypters.all()]

        new_secret_blob = encrypt(new_secret, public_keys)
        return RequestKeyRecovery.objects.create(uid=self, secret_blob=str(new_secret_blob), hash_info=hash_info)

    def add_restorers(self, password, encrypters: Union[QuerySet, List[Identity]]):
        message = add_encrypters(self.secret_blob, self, password, encrypters)

        self.secret_blob = str(message)
        for e in encrypters:
            self.encrypters.add(e)
        self.save()


class EncryptedMessageBase(models.Model):

    class Meta:
        abstract = True

    objects = EncryptedMessageManager()

    text = models.TextField()

    encrypters = models.ManyToManyField(
        Identity,
        help_text='The user doing the impersonating.',
        related_name='encrypted_keys',
    )

    @property
    def encrypted_text(self):
        return PGPMessage.from_blob(self.text)

    def can_decrypt(self, uid: Identity):
        return uid.id in [e.id for e in self.encrypters.all()]

    def encrypt(self, text, encrypters: Union[QuerySet, List[Identity]]):
        public_keys = [e.public_key for e in encrypters]
        pgp_msg = encrypt(text, public_keys)

        self.text = str(pgp_msg)
        self.save()

        for e in encrypters:
            self.encrypters.add(e)

        return pgp_msg

    def decrypt(self, uid: Identity) -> str:
        if not uid.private_key.is_unlocked:
            raise PGPError('Cannot decrypt with a protected key')

        if not self.can_decrypt(uid):
            raise PGPError('This UID is not in the list of encrypters')

        pgp_msg = PGPMessage.from_blob(self.text)
        return uid.private_key.decrypt(pgp_msg).message

    def add_encrypters(self, uid, password, encrypters: Union[QuerySet, List[Identity]]):
        message = add_encrypters(self.text, uid, password, encrypters)
        self.text = str(message)
        self.save()

        for e in encrypters:
            self.encrypters.add(e)

        return message

    def remove_encrypters(self, encrypters: Union[QuerySet, List[Identity]]):
        message = PGPMessage.from_blob(self.text)

        fingerprints_to_remove = [e.private_key.fingerprint.keyid for e in encrypters]
        message._sessionkeys = [pk for pk in message._sessionkeys if pk.encrypter not in fingerprints_to_remove]

        self.text = str(message)
        self.save()

        for e in encrypters:
            self.encrypters.remove(e)


class RequestKeyRecovery(models.Model):
    # pgp = PasswordResetManager()

    uid = models.ForeignKey(Identity,
                            on_delete=CASCADE,
                            related_name='reset_requests')

    reset_by = models.ForeignKey(Identity,
                                 on_delete=CASCADE,
                                 null=True,
                                 blank=True,
                                 related_name='password_reset_requests')

    secret_blob = models.TextField(null=True, blank=True)
    hash_info = models.CharField(max_length=32, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def get_secret(self, uid: Identity):
        return get_secret(uid, self.secret_blob)

    def reset_password(self, reset_by: Identity, uid_password: str):
        with reset_by.unlock(uid_password):
            if self.uid.encrypters.filter(id=reset_by.id).exists():
                old_secret = self.uid.get_secret(reset_by)
                new_secret = self.get_secret(reset_by)

                with self.uid.private_key.unlock(old_secret):
                    encrypt_private_key_by_password(self.uid.private_key, new_secret)

                self.uid.private_key_blob = str(self.uid.private_key)
                self.uid.hash_info = self.hash_info
                self.uid.secret_blob = self.secret_blob

                self.uid.save()
                self.finished(reset_by)

    def finished(self, uid):
        self.reset_by = uid
        self.finished_at = timezone.now()
        self.secret_blob = None
        self.hash_info = None

        self.save()
