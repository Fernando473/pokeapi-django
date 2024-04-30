from typing import Any

from pokeapi.utils.utils_mapper import from_str


class SpritesDto:
    back_default: str
    back_female: None
    back_shiny: str
    back_shiny_female: None
    front_default: str
    front_female: None
    front_shiny: str
    front_shiny_female: None

    def __init__(self, back_default, back_female, back_shiny, back_shiny_female,
                 front_default, front_female, front_shiny, front_shiny_female,
                 ):
        self.back_default = back_default
        self.back_female = back_female
        self.back_shiny = back_shiny
        self.back_shiny_female = back_shiny_female
        self.front_default = front_default
        self.front_female = front_female
        self.front_shiny = front_shiny
        self.front_shiny_female = front_shiny_female

    @staticmethod
    def from_json(obj: Any) -> 'SpritesDto':
        assert isinstance(obj, dict)
        back_default = from_str(obj.get("back_default"))
        back_female = from_str(obj.get("back_female"))
        back_shiny = from_str(obj.get("back_shiny"))
        back_shiny_female = from_str(obj.get("back_shiny_female"))
        front_default = from_str(obj.get("front_default"))
        front_female = from_str(obj.get("front_female"))
        front_shiny = from_str(obj.get("front_shiny"))
        front_shiny_female = from_str(obj.get("front_shiny_female"))
        return SpritesDto(back_default, back_female, back_shiny, back_shiny_female, front_default, front_female,
                          front_shiny, front_shiny_female)

    def to_json(self):
        return {
            "back_default": from_str( self.back_default),
            "back_female": from_str(self.back_female),
            "back_shiny":  from_str(self.back_shiny),
            "back_shiny_female": from_str(self.back_shiny_female),
            "front_default": from_str(self.front_default),
            "front_female": from_str(self.front_female),
            "front_shiny": from_str( self.front_shiny),
            "front_shiny_female": from_str(self.front_shiny_female)
        }