from random import choices


def generate(length=1) -> str:
    return ''.join(choices('abcdefghijklmnopqrstuvwxyz0123456789', k=length))
