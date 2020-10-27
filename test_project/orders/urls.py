from .views import order_list, order_detail
from django.urls import path

urlpatterns = [
    path('api/orders', order_list),
    path('api/orders/<int:pk>', order_detail),
]
