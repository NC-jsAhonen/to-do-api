from rest_framework import serializers

from todo.models import Item, List

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'done', 'text', 'list']

class ListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = List
        fields = ['id','items']
