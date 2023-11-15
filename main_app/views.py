

from django.shortcuts import render
from django.views.generic import DetailView,ListView
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

