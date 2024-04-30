from typing import Any

from pokeapi.utils.utils_mapper import from_str, from_bool


class AbilitiesDto:
    name: str
    is_hidden: bool

    def __init__(self, name, is_hidden):
        self.name = name
        self.is_hidden = is_hidden

    @staticmethod
    def from_json(abilities_list):
        abilities = []
        for ability_data in abilities_list:
            assert isinstance(ability_data, dict)
            name = from_str(ability_data['ability']['name'])
            is_hidden = from_bool(ability_data['is_hidden'])
            abilities.append(AbilitiesDto(name, is_hidden))
        return abilities

    def to_json(self) -> dict:
        result: dict = {"name": from_str(self.name), "is_hidden": from_bool(self.is_hidden)}
        return result
