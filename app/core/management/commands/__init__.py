from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Django management command to wait for database service initialization.
    """

    def handle(self, *args, **options):
        pass
