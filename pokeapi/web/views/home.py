from django.http import JsonResponse
from django.shortcuts import render
from pokeapi.service.pokemons_service import PokemonService


# Create your views here.

def home(request):
    try:
        service = PokemonService()
        url = request.GET.get('url')
        current_page = request.GET.get('current_page', 1)
        pokemons, response_dto, total_pages = service.fetch_pokemons(url=url, page_size=20)
        remaining_pages = request.GET.get('remaining_pages', int(total_pages))

        context = {'pokemons': pokemons, 'total_pages': int(total_pages), 'response': response_dto,
                   'current_page': current_page, 'remaining_pages': remaining_pages}

        return render(request, "home.html", context=context)
    except Exception as e:
        return JsonResponse({'message': f'Something went wrong: {e}'})
