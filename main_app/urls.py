from django.urls import path

from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.game_list, name="game_list_main_page"),
    path(
        "<slug:category_slug>/",
        views.game_list,
        name="game_list_by_category",
    ),
    path("game/<int:id>/<slug:slug>/", views.game_detail, name="game_detail"),
    # path("about/", views.about_page, name="about"),
    # path("faq/", views.faq_page, name="faq"),
    # path("top_game/", views.top_game_page, name="top_game"),
    path("search/", views.Search.as_view, name="search"),
]
