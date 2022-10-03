from pytest_factoryboy import register

from .factories import ReviewFactory

for factory in (ReviewFactory,):
    register(factory)
