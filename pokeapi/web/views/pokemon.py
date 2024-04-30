from django.shortcuts import render

from pokeapi.service.pokemons_service import PokemonService


def pokemon_details(request, pokemon_id):
    service = PokemonService()
    pokemon = service.fetch_pokemon_by_id(pokemon_id)
    context = {
        'pokemon': pokemon
    }
    return render(request, template_name="pokemon/pokemon_base.html", context=context)
