from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = "Minister"

    # Starts signals to create minister profile.
    def ready(self):
        from . import signals
