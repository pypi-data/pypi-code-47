from importlib import import_module

import django.apps


class AppConfig(django.apps.AppConfig):
    """ An extended version of DJango's AppConfig container. """

    def ready(self):
        super().ready()

        # Run model extension code
        try:
            import_module(
                ".".join(self.__class__.__module__.split(".")[:-1] + ["model_extensions"])
            )
        except ImportError:
            # ImportErrors are non-fatal because model extensions are optional.
            pass
