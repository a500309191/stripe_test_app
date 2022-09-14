from django.urls import path, re_path, include
from . import views
from rest_framework import routers
from . views import ItemsViewSet

router = routers.DefaultRouter()
router.register(r"items", ItemsViewSet, basename="item")

urlpatterns = [
    path("api/", include(router.urls)),
    path('buy/<int:item_id>', views.buy_one),
    path('buy_bunch/<str:items_id>', views.buy_bunch),
    path('success/<int:order_id>', views.success),
    path('cancel/<int:order_id>', views.cancel),
]

