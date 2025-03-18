from django.db import models
from menu.models import Menu

STATUS = ((0, "Ordered"), (1, "Preparing"), (2, "Done"))


# Create your models here.
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())


class OrderCart(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items'
    )
    customer_order = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='order_cart'
    )
    status = models.IntegerField(choices=STATUS, default=0)

    def get_total_price(self):
        return self.menu.price * self.status
