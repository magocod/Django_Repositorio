#fechas
from datetime import date
from datetime import datetime

#señales
from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver

#modelos
from backend.storage.models import Item_type, Tag, Collection, Item, Category, Theme


@receiver(pre_save, sender=Item)
def actual_items(sender, instance, **kwargs):
    instance.actualizado = date.today()
    instance.save()
