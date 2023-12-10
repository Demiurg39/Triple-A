from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from cart.forms import CartAddGameForm
from .forms import CommentForm
from .models import Category, Games, SystemRequirements


def game_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    games = Games.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        games = Games.objects.filter(category=category, available=True)
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
            "category": category,
            "categories": categories,
            "page": page,
        },
    )


@login_required
def add_comment(request, slug):
    game = get_object_or_404(Games, slug=slug)
    comment = None
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.game = game
            comment.save()
        return redirect("main_app:game_detail", slug=slug)
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
        query = self.request.GET.get("q")
        if query:
            # Используем оператор Q для объединения условий поиска
            return Games.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        else:
            return Games.objects.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context
