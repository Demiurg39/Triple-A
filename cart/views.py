from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from main_app.models import Games

from .cart import Cart
from .forms import CartAddGameForm


@require_POST
def cart_add(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Games, id=game_id)
    form = CartAddGameForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            game=game,
            quantity=cd["quantity"],
            override_quantity=cd["quantity"],
        )
    return redirect("cart:cart_detail")


@require_POST
def cart_remove(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Games, id=game_id)
    cart.remove(game)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/detai.html", {"cart": cart})