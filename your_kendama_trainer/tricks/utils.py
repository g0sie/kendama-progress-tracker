from faker import Faker
from faker.providers import DynamicProvider
from random import randint

from .models import Trick


def add_fake_tricks(n=10):
    trick_difficulty_provider = DynamicProvider(
        provider_name="trick_difficulty",
        elements=['beginner', 'intermediate', 'advanced', 'other'],
    )
    fake = Faker()
    fake.add_provider(trick_difficulty_provider)

    for _ in range(n):
        Trick.objects.create(
            name=fake.text(randint(5, 100)),
            difficulty=fake.trick_difficulty(),
            official=False
        )
