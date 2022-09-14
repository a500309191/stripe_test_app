from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    #currency = models.IntegerField(choices=((1, "usd"), (2, "yuan"),))

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    status = models.CharField(max_length=20, default="before_payment")
    created = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"{self.__class__}: {self.status}"

    def __str__(self):
        return f"{self.status}"


class Item_Order(models.Model):
    item_quantity = models.IntegerField()
    item = models.ForeignKey("Item", on_delete=models.DO_NOTHING)
    order = models.ForeignKey("Order", on_delete=models.DO_NOTHING)

    def __repr__(self):
        return f"{self.__class__}: {self.order_id}"

    def __str__(self):
        return f"order: {self.order_id} item:{self.item_id}x{self.item_quantity}"