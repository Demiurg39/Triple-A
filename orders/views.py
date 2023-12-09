from django.shortcuts import render

from cart.cart import Cart

from .forms import OrderCreateForm
from .models import OrderItem


def order_create(request):
    cart = Cart()
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    game=item["game"],
                    price=item["price"],
                    quantity=["quantity"],
                )

            cart.clear()
            return render(request, "orders/order/created.html", {"order": order})

        else:
            form = OrderCreateForm()
        return render(request, "orders/order/create.html", {"cart": cart, "form": form})
