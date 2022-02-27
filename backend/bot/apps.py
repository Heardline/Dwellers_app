from django.apps import AppConfig

def register(dp: Optional[Dispatcher] = None) -> None:
    """
    The function registers the app.
    :param dp:
        If Dispatcher is not None — register bots modules.
    """

    if dp is not None:
        from .filters import register_filters
        from bot.handlers import register_handlers

        register_filters(dp)
        register_handlers(dp)


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'
