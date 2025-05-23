from django.apps import AppConfig


class AUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_app'
    
    def ready(self):
        import users_app.signals
