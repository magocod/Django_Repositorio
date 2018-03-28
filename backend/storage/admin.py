from django.contrib import admin

#modelos
from backend.storage.models import Item, Collection, Tag, Item_type, Category, Theme

# Register your models here.

admin.site.register(Item)

admin.site.register(Theme)

admin.site.register(Category)

admin.site.register(Collection)

admin.site.register(Tag)

admin.site.register(Item_type)

