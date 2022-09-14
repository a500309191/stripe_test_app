from django.contrib import admin
from . models import Item, Order


# admin.site.register(Item)
admin.site.register(Order)


@admin.register(Item)
class ImageAdmin(admin.ModelAdmin):
    exclued = ["order"]
