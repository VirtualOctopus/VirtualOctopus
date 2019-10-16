from .base_sucker import BaseSucker
from .http_sucker import HTTPSucker
from typing import Optional

__all_suckers = {}


def register_sucker(sucker: BaseSucker, schema: Optional[str] = None):
    if schema is None:
        __all_suckers[sucker.get_schema()] = sucker
    else:
        __all_suckers[schema] = sucker


def get_sucker(schema: str) -> BaseSucker:
    return __all_suckers.get(schema)


register_sucker(HTTPSucker, "https")
register_sucker(HTTPSucker)
