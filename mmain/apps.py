from django.apps import AppConfig


class MmainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mmain'

    def ready(self):
        import mmain.signals
