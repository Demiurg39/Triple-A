

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Games


def main_page(request):
   game = Games.objects.order_by()
   return render(request,'main_app.html', {'main_page': game})

class GamesDetailView(DetailView):
    model = Games.objects.all()
    template_name = 'details_view.html'
    context_object_name = 'games'

def about_page(request):
    return render(request, 'about_page.html')

def faq_page(request):
    return render(request, 'faq_page.html')

def cart_page(request):
    return render(request, 'cart_page.html')

def auth_page(request):
    return render(request, 'auth_page.html')

def top_game_page(request):
    return render(request, 'top_game_page.html')