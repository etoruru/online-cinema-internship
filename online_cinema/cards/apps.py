from django.apps import AppConfig


class CardsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cards"

    def ready(self):
        try:
            import online_cinema.cards.signals  # noqa F401
        except ImportError:
            pass
