from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Games


def main_page(request):
    game = Games.objects.order_by()
    return render(request, "main_app.html", {"main_page": game})


class GamesDetailView(DetailView):
    model = Games
    template_name = "details_view.html"
    context_object_name = "games"


class Search(ListView):
    template_name = "main_app.html"
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


def cart_page(request):
    return render(request, "cart_page.html")


def top_game_page(request):
    return render(request, "top_game_page.html")
