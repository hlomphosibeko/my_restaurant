from django.urls import path
from .views import order_cart_add, cart_detail


app_name = "order_cart"
urlpatterns = [
    path('add/<int:menu_id>/', order_cart_add, name='order_cart_add'),
    path('', cart_detail, name='cart_detail')
]
