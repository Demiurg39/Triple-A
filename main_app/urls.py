from django.urls import path

from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path(
        "game/<slug:slug>/",
        views.GamesDetailView.as_view(),
        name="game_detail",
    ),
    path("about/", views.about_page, name="about"),
    path("faq/", views.faq_page, name="faq"),
    path("cart/", views.cart_page, name="cart"),
    path("top_game/", views.top_game_page, name="top_game"),
    path("search/", views.Search.as_view, name="search"),
]
