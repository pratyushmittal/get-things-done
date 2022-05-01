import factory
from factory.django import DjangoModelFactory

from boards.models import Board


class BoardFactory(DjangoModelFactory):
    class Meta:
        model = Board

    ip = "1.1.1.1"
    slug = factory.LazyAttributeSequence(lambda o, n: f"board-{n}")
