from django.core.management.base import BaseCommand
from tricks.models import Tutorial


class Command(BaseCommand):
    help = 'adds new tutorials to database'

    def handle(self, **options):
        self.stdout.write(self.style.SUCCESS('komenda działa'))
