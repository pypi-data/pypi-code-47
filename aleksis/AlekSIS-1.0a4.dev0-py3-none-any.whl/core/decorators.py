from typing import Callable

from django.contrib.auth.decorators import user_passes_test


def admin_required(function: Callable = None) -> Callable:
    actual_decorator = user_passes_test(lambda u: u.is_active and u.is_superuser)
    return actual_decorator(function)
