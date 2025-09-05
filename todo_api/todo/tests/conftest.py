import pytest
from pytest_factoryboy import register
from todo.tests.factories import ListFactory, ItemFactory

register(ListFactory)
register(ItemFactory)