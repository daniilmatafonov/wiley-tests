# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome1_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Page:
    id: str
    boost: float
    title: str
    url: str
    content: str

    def __init__(self, id: str, boost: float, title: str, url: str, content: str) -> None:
        self.id = id
        self.boost = boost
        self.title = title
        self.url = url
        self.content = content

    @staticmethod
    def from_dict(obj: Any) -> 'Page':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        boost = from_float(obj.get("boost"))
        title = from_str(obj.get("title"))
        url = from_str(obj.get("url"))
        content = from_str(obj.get("content"))
        return Page(id, boost, title, url, content)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["boost"] = to_float(self.boost)
        result["title"] = from_str(self.title)
        result["url"] = from_str(self.url)
        result["content"] = from_str(self.content)
        return result


class Suggestion:
    term: str

    def __init__(self, term: str) -> None:
        self.term = term

    @staticmethod
    def from_dict(obj: Any) -> 'Suggestion':
        assert isinstance(obj, dict)
        term = from_str(obj.get("term"))
        return Suggestion(term)

    def to_dict(self) -> dict:
        result: dict = {}
        result["term"] = from_str(self.term)
        return result


class SearchResponse:
    suggestions: List[Suggestion]
    products: List[Any]
    pages: List[Page]
    show_see_all_products: bool
    show_see_all_pages: bool

    def __init__(self, suggestions: List[Suggestion], products: List[Any], pages: List[Page], show_see_all_products: bool, show_see_all_pages: bool) -> None:
        self.suggestions = suggestions
        self.products = products
        self.pages = pages
        self.show_see_all_products = show_see_all_products
        self.show_see_all_pages = show_see_all_pages

    @staticmethod
    def from_dict(obj: Any) -> 'SearchResponse':
        assert isinstance(obj, dict)
        suggestions = from_list(Suggestion.from_dict, obj.get("suggestions"))
        products = from_list(lambda x: x, obj.get("products"))
        pages = from_list(Page.from_dict, obj.get("pages"))
        show_see_all_products = from_bool(obj.get("showSeeAllProducts"))
        show_see_all_pages = from_bool(obj.get("showSeeAllPages"))
        return SearchResponse(suggestions, products, pages, show_see_all_products, show_see_all_pages)

    def to_dict(self) -> dict:
        result: dict = {}
        result["suggestions"] = from_list(lambda x: to_class(Suggestion, x), self.suggestions)
        result["products"] = from_list(lambda x: x, self.products)
        result["pages"] = from_list(lambda x: to_class(Page, x), self.pages)
        result["showSeeAllProducts"] = from_bool(self.show_see_all_products)
        result["showSeeAllPages"] = from_bool(self.show_see_all_pages)
        return result


def search_response_from_dict(s: Any) -> SearchResponse:
    return SearchResponse.from_dict(s)


def search_response_to_dict(x: SearchResponse) -> Any:
    return to_class(SearchResponse, x)