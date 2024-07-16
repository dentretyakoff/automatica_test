import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    """Создание админа."""
    help = 'Создание админа.'

    def handle(self, *args, **kwarg):
        username = os.getenv('ADMIN_USER')
        password = os.getenv('ADMIN_PASSWORD')
        email = os.getenv('ADMIN_EMAIL')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            User.objects.create_superuser(
                username=username,
                password=password,
                email=email)
            self.stdout.write(
                self.style.SUCCESS(f'Создан пользователь {username}'))
