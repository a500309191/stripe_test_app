from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Item, Order, Item_Order
import stripe
from rest_framework import viewsets
from . serializers import ItemsSerializer
from decouple import config
from django.conf import settings


stripe.api_key = config("STRIPE_API_KEY")

if settings.DEBUG:
    address = "localhost:8000"
else: 
    address = config("HOST")

class ItemsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer


def buy_one(request, item_id):

    new_order = Order.objects.create()
    item = Item.objects.get(id=item_id)

    new_item_order = Item_Order.objects.create(
        order_id=new_order.id,
        item_id=item.id,
        item_quantity=1,
    )

    session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": f"{item.name}",
                        "description": f"{item.description}",
                    },
                    "unit_amount": item.price,
                },
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url=f"http://{address}/success/{new_order.id}",
        cancel_url=f"http://{address}/cancel/{new_order.id}",
    )

    return HttpResponseRedirect(session.url)


def buy_bunch(request, items_id):

    complex_items = items_id.split("+")
    line_items = []

    new_order = Order.objects.create()

    for complex_item in complex_items:
        split_item = complex_item.split("n")

        item_id = split_item[0]
        item_quantity = split_item[1]

        item = Item.objects.get(id=item_id)

        new_item_order = Item_Order.objects.create(
            order_id=new_order.id,
            item_id=item.id,
            item_quantity=item_quantity,
        )

        line_item = {
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": f"{item.name}",
                    "description": f"{item.description}",
                },
                "unit_amount": item.price,
            },
            "quantity": f"{item_quantity}",
        }

        line_items.append(line_item)

    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode="payment",
        success_url=f"http://{address}/success/{new_order.id}",
        cancel_url=f"http://{address}/cancel/{new_order.id}",
    )

    return HttpResponseRedirect(session.url)


def payment_response(request, order_id, status):
    order = Order.objects.get(id=order_id)
    if order.status == "before_payment":
        order.status = status
        order.save()

    refs = Item_Order.objects.filter(order_id = order.id)

    items = [
        {
            "name": Item.objects.get(id=ref.item_id).name,
            "multiple_price": round(Item.objects.get(id=ref.item_id).price*ref.item_quantity/100, 2),
            "quantity": ref.item_quantity,
        }
        for ref in refs
    ]
    total_quantity = sum([item["quantity"] for item in items])
    total_price = round(sum([item["multiple_price"] for item in items]), 2)

    return render(
        request,
        f"{status}.html",
        {
            "items": items,
            "total_quantity": total_quantity,
            "total_price": total_price,
        }
    )


def success(request, order_id):
    return payment_response(request, order_id, "success")

def cancel(request, order_id):
    return payment_response(request, order_id, "cancel")
