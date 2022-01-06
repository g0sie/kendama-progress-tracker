from django.core.management.base import BaseCommand

from tricks.utils import add_fake_tricks


class Command(BaseCommand):
    help = "Add n fake tricks to database"

    def handle(self, *args, **options):
        n = options.get('number', 10)
        add_fake_tricks(n)
        self.stdout.write(f"{n} tricks have been added")

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--number',
            type=int, default=10, dest='number',
            help="Amount of tricks to add"
        )
