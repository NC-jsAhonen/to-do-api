from django.contrib import admin

from todo.models import Item, List

admin.site.register(Item)
admin.site.register(List)