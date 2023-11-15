from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page , name='main_page'),
    path('<str:title>/<int:pk>', views.GamesDetailView.as_view(), name='game-detail'),
    path('/about', views.about_page, name='about')
]