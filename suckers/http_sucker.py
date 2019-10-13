from uri import URI

from contents.http_content import HTTPContent

from suckers.base_sucker import BaseSucker

import requests


class HTTPSucker(BaseSucker):

    @classmethod
    def get_schema(self) -> str:
        return "http"

    def get_content(self, uri: URI, options: dict) -> HTTPContent:
        response = requests.request(options.get("method"), uri)
        return HTTPContent(response.text,
                           response.headers,
                           response.status_code)
