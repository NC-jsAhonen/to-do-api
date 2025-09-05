from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from todo.models import Item, List
from todo.serializers import ItemSerializer, ListSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=True, methods=["patch"])
    def check(self, request, pk=None):
        """Toggle the 'done' status of an item."""
        item = self.get_object()
        item.toggle_done()
        item.save()
        serializer = self.get_serializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
