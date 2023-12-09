from django.urls import path
from . import views

urlpatterns = [
    path('rent_game/<int:id>/<slug:slug>/', views.rent_game, name='rent_game'),
]
