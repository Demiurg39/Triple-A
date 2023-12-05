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
    path("search/", views.Search.as_view(), name="search"),
    path(
        "game/<int:id>/<slug:slug>/add_comment/",
        views.add_comment,
        name="add_comment",
    ),
]
