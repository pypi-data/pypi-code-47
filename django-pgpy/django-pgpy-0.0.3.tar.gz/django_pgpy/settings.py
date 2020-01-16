from django.conf import settings
from pgpy.constants import KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm

from django_pgpy.defaults import get_default_restorers

DJANGO_PGPY_DEFAULT_RESTORERS = getattr(settings, 'DJANGO_PGPY_DEFAULT_RESTORERS', get_default_restorers)

DJANGO_PGPY_KEY_USAGE = getattr(settings, 'DJANGO_PGPY_KEY_USAGE', {
    KeyFlags.Sign,
    KeyFlags.EncryptCommunications,
    KeyFlags.EncryptStorage
})

DJANGO_PGPY_KEY_HASHES = getattr(settings, 'DJANGO_PGPY_KEY_HASHES', [
    HashAlgorithm.SHA256,
    HashAlgorithm.SHA384,
    HashAlgorithm.SHA512,
    HashAlgorithm.SHA224
])

DJANGO_PGPY_KEY_CIPHERS = getattr(settings, 'DJANGO_PGPY_KEY_CIPHERS', [
    SymmetricKeyAlgorithm.AES256,
    SymmetricKeyAlgorithm.AES192,
    SymmetricKeyAlgorithm.AES128
])

DJANGO_PGPY_KEY_COMPRESSION = getattr(settings, 'DJANGO_PGPY_KEY_COMPRESSION', [
    CompressionAlgorithm.ZLIB,
    CompressionAlgorithm.BZ2,
    CompressionAlgorithm.ZIP,
    CompressionAlgorithm.Uncompressed
])
