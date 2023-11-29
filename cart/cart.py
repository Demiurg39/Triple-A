from decimal import Decimal

from django.conf import settings

from main_app.models import Games


class Cart:
    def __init__(self, request):
        """INIT CART"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """ITER ITEMS IN THE CART AND GET ITEMS FROM DB"""
        game_ids = self.cart.keys()
        games = Games.objects.filter(id__in=game_ids)
        cart = self.cart.copy()
        for game in games:
            cart[str(game.id)]["game"] = game
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """SUM ALL ITEMS IN CART"""
        return sum(item["quantity"] for item in self.cart.values())
        pass

    def add(self, game, quantity=1, override_quantity=False):
        """ADD TO ITEM TO CART"""
        game_id = str(game.id)
        if game_id not in self.cart:
            self.cart[game_id] = {
                "quantity": 0,
                "price": str(game.price),
            }

        if override_quantity:
            self.cart[game_id]["quantity"] = quantity

        else:
            self.cart[game_id]["quantity"] += quantity

    def save(self):
        """TO MARKUP SESSION MODIFIED"""
        self.session.modified = True

    def remove(self, game):
        """REMOVE ITEM FROM THE CART"""
        game_id = str(game.id)
        if game_id in self.cart:
            del self.cart[game_id]
            self.save()

    def clear(self):
        """CLEAR CART"""
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        """GET TOTAL PRICE OF ALL ITEMS IN CART"""
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )
