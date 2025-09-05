import factory

from todo.models import Item, List

class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item
    done = False
    text = "Example"
    

class ListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = List
