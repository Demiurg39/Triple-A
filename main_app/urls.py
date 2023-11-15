from django.urls import path
from . import views
from .views import GamesDetailView

urlpatterns = [
    path('', views.main_page , name='main_page'),
    path('<int:pk>', views.GamesDetailView.as_view(), name='game-detail'),
]