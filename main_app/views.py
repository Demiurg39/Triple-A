from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView

from cart.forms import CartAddGameForm

from .forms import CommentForm
from .models import Category, Games


def game_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    games = Games.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        games = Games.objects.filter(categories=category, available=True)
    post_list = Games.objects.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page")
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(
        request,
        "game_list.html",
        {
            "games": games,
            "category": category,
            "categories": categories,
            "page": page,
        },
    )


@login_required
def add_comment(request, id, slug):
    game = get_object_or_404(Games, id=id, slug=slug)
    comment = None
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.game = game
            comment.save()
            return redirect(reverse("main_app:game_detail", args=[game.id, game.slug]))
    else:
        form = CommentForm()
    return render(
        request,
        "add_comment.html",
        {
            "form": form,
            "game": game,
            "comment": comment,
        },
    )


def game_detail(request, id, slug):
    game = get_object_or_404(Games, id=id, slug=slug, available=True)
    cart_game_form = CartAddGameForm()
    game_price = float(game.price)
    rental_price = round(0.05 * game_price * 7, 2)
    return render(
        request,
        "details_view.html",
        {
            "game": game,
            "cart_game_form": cart_game_form,
            "rental_price": rental_price,
        },
    )


class Search(ListView):
    template_name = "search_results.html"
    context_object_name = "games"
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Games.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            ).filter(
                available=True
            )  # фильтр для доступных игр, если это нужно
        else:
            return Games.objects.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context


def top_games(request):
    top_rated_games = Games.objects.filter(available=True).order_by("-rating")[:5]
    return render(
        request,
        "top_game_page.html",
        {"top_rated_games": top_rated_games},
    )
