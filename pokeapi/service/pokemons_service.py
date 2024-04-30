from typing import List

from pokeapi.dto.pokemon_dto import PokemonDto
from pokeapi.dto.response_dto import ResponseDto
from pokeapi.utils.utils_request import do_get

import concurrent.futures
from functools import partial


class PokemonService:
    url = "https://pokeapi.co/api/v2/pokemon/"

    def fetch_pokemons(self, url=None, page=1, page_size=20):

        offset = (page - 1) * page_size

        if url:
            self.url = url

        response = do_get(self.url, limit=page_size)

        response_dto = ResponseDto.from_json(response)
        total_pages = response_dto.count / len(response_dto.results)

        pokemon_urls = [result.get("url") for result in response_dto.results]

        pokemons = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_url = {executor.submit(self.fetch_pokemon, url): url for url in pokemon_urls}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    pokemon = future.result()
                    pokemons.append(pokemon)
                except Exception as e:
                    print(f"Error fetching data for {url}: {e}")

        return pokemons, response_dto, total_pages

    def fetch_pokemon(self, url):
        try:

            self.url = url
            pokemon_response = do_get(self.url)
            return PokemonDto.from_json(pokemon_response)
        except Exception as e:
            return Exception(e)

    def fetch_pokemon_by_id(self, pokemon_id):
        try:
            url = f'{self.url}{pokemon_id}'
            response = do_get(url)
            return PokemonDto.from_json(response)
        except Exception as e:
            return Exception(e)
