import factory
from factory import Faker

from crawler.gp_crawler.models import Review

faker = Faker(["en"])


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    id = factory.Faker("uuid4")
    user_name = factory.Faker("first_name")
    content = factory.Faker("sentence")
    score = factory.Faker("pyint")
