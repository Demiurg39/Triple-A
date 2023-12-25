import uuid
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from keys.models import Keys
from main_app.models import Games
from .forms import RentKeyForm
from .tasks import send_rental_key_email


def rent_game(request, id, slug):
    game = get_object_or_404(Games, id=id, slug=slug)

    if request.method == "POST":
        form = RentKeyForm(request.POST)
        if form.is_valid():
            rental_days = form.cleaned_data["period"]
            unique_code = uuid.uuid4().hex[:12]

            try:
                rental_key = Keys.objects.create(
                    game=game, user=request.user, period=rental_days, code=unique_code
                )

                rental_price = rental_key.calculate_rent_price()

                # Отправляем ключ на почту
                send_rental_key_email.delay(request.user.email, rental_key.code)

                # Обновляем статус ключа на "отправлен"
                rental_key.status = "sent"
                rental_key.save()

                # Выводим сообщение об успешной аренде
                messages.success(
                    request,
                    f"Игра '{game.name}' успешно арендована! Ключ отправлен на вашу почту.",
                )

                return HttpResponseRedirect(
                    reverse("cart:cart_detail") + f"rental_price={rental_price}"
                )

            except Exception as e:
                messages.error(request, f"Произошла ошибка при аренде игры: {e}")

    else:
        form = RentKeyForm()

    return render(request, "keys/rent_game.html", {"form": form, "game": game})
