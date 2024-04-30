from django.urls import path

from pokeapi.web.views import home
from pokeapi.web.views import pokemon

urlpatterns = [
    path('', home.home, name="home"),
    path('pokemon/<int:pokemon_id>', pokemon.pokemon_details, name="pokemon_details")
]
