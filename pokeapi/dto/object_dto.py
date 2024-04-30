from typing import List, Any


from pokeapi.utils.utils_mapper import from_str


class ObjectDto:
    name: str
    poke_url = str

    def __init__(self, name, poke_url):
        self.name = name
        self.poke_url = poke_url

    @staticmethod
    def from_json(obj: Any) -> 'ObjectDto':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        poke_url = from_str(obj.get("url"))
        return ObjectDto(name, poke_url)

