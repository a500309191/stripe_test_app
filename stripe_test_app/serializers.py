from rest_framework import serializers
from . models import Item


class ItemsSerializer(serializers.ModelSerializer):

    currency = serializers.CharField(source='get_currency_display', read_only=True)

    class Meta:
        model = Item
        fields = "__all__"