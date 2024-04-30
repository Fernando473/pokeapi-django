from typing import Any

from pokeapi.utils.utils_mapper import from_str, from_int


class ResponseDto:
    count: int
    previous_page: str
    next_page: str
    results: dict

    def __init__(self, count, previous_page, next_page, results):
        self.count = count
        self.previous_page = previous_page
        self.next_page = next_page
        self.results = results

    @staticmethod
    def from_json(obj: Any):
        assert isinstance(obj, dict)
        count = from_int(obj.get('count'))
        previous_page = from_str(obj.get('previous'))
        next_page = from_str(obj.get('next'))
        results = obj.get('results')
        return ResponseDto(count, previous_page, next_page, results)

    def to_json(self):
        return {
            "count": self.count,
            "previous_page": self.previous_page,
            "next_page": self.next_page,
            "results": self.results,

        }
