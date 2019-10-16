from uri import URI

from octopus.contents.http_content import HTTPContent
from typing import List
from octopus.suckers.base_sucker import BaseSucker

import requests


class HTTPSucker(BaseSucker):

    @classmethod
    def get_schema(cls) -> str:
        return "http"

    def get_contents(self, uri: URI, options: dict) -> List[HTTPContent]:
        response = requests.request(options.get("method"), uri)
        return [HTTPContent(response.text,
                            response.headers,
                            response.status_code)]
