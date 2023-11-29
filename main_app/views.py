from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from cart.forms import CartAddGameForm

from .models import Category, Games, SystemRequirements


def game_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    games = Games.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        games = Games.objects.filter(category=category, available=True)

    return render(
        request,
        "game_list.html",
        {
            "category": category,
            "categories": categories,
            "games": games,
        },
    )


def game_detail(request, id, slug):
    game = get_object_or_404(Games, id=id, slug=slug, available=True)
    cart_game_form = CartAddGameForm()
    return render(
        request,
        "details_view.html",
        {
            "game": game,
            "cart_game_form": cart_game_form,
        },
    )


class Search(ListView):
    template_name = "game_list.html"
    context_object_name = "games"
    paginate_by = 5

    def get_queryset(self):
        return Games.objects.filter(title__icontans=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context


def about_page(request):
    return render(request, "about_page.html")


def faq_page(request):
    return render(request, "faq_page.html")


def top_game_page(request):
    return render(request, "top_game_page.html")
