from django.shortcuts import render, get_object_or_404
from menu.models import Menu
from .models import Cart, OrderCart
from django.views.decorators.http import require_POST


# Create your views here.
@require_POST
def order_cart_add(request, menu_id):
    cart_id = request.session.get('cart_id')

    if cart_id:
        try:
            cart = Cart. objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    menu = get_object_or_404(Menu, id=menu_id)

    order_cart, created = OrderCart.objects.get_or_create(cart=cart, menu=menu)

    if not created:
        order_cart.status += 1

    order_cart.save()

    response_data = {
        "success": True,
        "message": f"Added {menu.menu_title} to cart"
    }

    return (response_data)


def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart = None

    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)

    return render(request, "ordercart/cart_detail.html", {"cart": cart})
