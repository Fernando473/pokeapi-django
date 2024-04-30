from typing import Any, List

from pokeapi.dto.abilities_dto import AbilitiesDto
from pokeapi.dto.sprite_dto import SpritesDto
from pokeapi.dto.stat_dto import Stat
from pokeapi.utils.utils_mapper import from_str, from_int


class PokemonDto:
    id: int
    name: str
    abilities: List[AbilitiesDto]
    sprites: SpritesDto
    height: str
    weight: str
    stats = List[Stat]

    def __init__(self, id, name, abilities, sprites, height, weight, stats):
        self.id = id
        self.sprites = sprites
        self.abilities = abilities
        self.name = name
        self.height = height
        self.weight = weight
        self.stats = stats

    @staticmethod
    def from_json(obj: Any) -> 'PokemonDto':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        sprites = SpritesDto.from_json(obj.get("sprites"))
        name = from_str(obj.get("name"))
        abilities = AbilitiesDto.from_json(obj.get("abilities"))
        height = from_int(obj.get("height"))
        weight = from_int(obj.get("weight"))
        stats = Stat.from_json(obj.get("stats"))
        return PokemonDto(id, name, abilities, sprites, height, weight, stats)

    def to_json(self):
        abilities_json = [ability.to_json() for ability in self.abilities]

        return {
            "name": self.name,
            "abilities": abilities_json,
            "sprites": self.sprites.to_json()
        }
