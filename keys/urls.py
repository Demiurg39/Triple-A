from django.urls import path
from . import views

app_name = 'keys'

urlpatterns = [
    path('rent_game/<int:id>/<slug:slug>/', views.rent_game, name='rent_game'),
]
