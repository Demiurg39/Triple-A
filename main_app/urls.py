from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page , name='main_page'),
    path('<str:title>/<int:pk>', views.GamesDetailView.as_view(), name='game-detail'),
    path('/about', views.about_page, name='about'),
    path('/faq', views.faq_page, name='faq'),
    path('/cart', views.cart_page, name='cart'),
    path('/authorization', views.auth_page, name='auth'),
    path('/top_game', views.top_game_page, name='top_game')
]