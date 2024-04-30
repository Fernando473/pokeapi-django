from pokeapi.utils.utils_mapper import from_str, from_int


class Stat:
    base_stat: int
    name: str

    def __init__(self, base_stat, name):
        self.base_stat = base_stat
        self.name = name

    @staticmethod
    def from_json(stats_list):
        stats = []
        for obj in stats_list:
            assert isinstance(obj, dict)
            base_stat = from_int(obj.get("base_stat"))
            name = from_str(obj.get("stat").get("name"))
            stats.append(Stat(base_stat, name))
        return stats
