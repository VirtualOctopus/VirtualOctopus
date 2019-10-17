from uri import URI
from lxml import etree
from json import loads
from octopus.contents.http_content import HTTPContent
from typing import List
from octopus.suckers.base_sucker import BaseSucker
from .content_type import ContentType, is_image, is_doc, is_text_content
from mimetypes import guess_type

import requests


class HTTPSucker(BaseSucker):

    """
    http sucker, retrieve data from remote

    detect:

    * file download

    * json api (list/object)

    * xml api (list/object)

    * traditional article

    * article list

    """

    @classmethod
    def get_schema(cls) -> str:
        return "http"

    def __get_content_type(self, h_content_type=None):
        content_type = ContentType.unknown

        if h_content_type.find("json") > -1:
            content_type = ContentType.json
        elif h_content_type.find("xml") > -1:
            content_type = ContentType.xml
        elif h_content_type.find("html") > -1:
            content_type = ContentType.html

        return content_type

    def __get_content_type_from_content(self, content=""):
        content = content.strip()
        content_type = ContentType.unknown

        if len(content) == 0:
            content_type = ContentType.empty

        if (content_type is ContentType.unknown and content.startswith("<") and content.endswith(">")):

            try:
                etree.fromstring(content_type)  # try parse it
                content_type = ContentType.xml
            except:
                pass

        if (content_type is ContentType.unknown and content.startswith("[") or content.startswith("{")):
            try:
                loads(content_type)  # try parse it
                content_type = ContentType.json
            except:
                pass

        return content_type

    def __is_list(self, content_type=ContentType.unknown, content_text=None):
        pass

    def get_contents(self, uri: URI, options: dict) -> List[HTTPContent]:

        response = requests.request(options.get("method"), uri)

        h_content_type = response.headers.get("content-type")

        if "content-disposition" in response.headers:
            # server want to send file to client
            content_type = ContentType.binary
        else:
            content_type = self.__get_content_type(h_content_type)

        if is_text_content(content_type):
            # if response is text
            content_text = response.text
            content_type_2 = self.__get_content_type_from_content(content_text)
            if content_type_2 == content_type:
                pass
            else:
                # raise error
                pass

        if content_type == ContentType.binary:
            # for binary file
            (mimetype, encoding) = guess_type(uri)
            if is_image(mimetype):
                pass
            elif is_doc(mimetype):
                pass

        return [HTTPContent(response.text, response.headers, response.status_code)]
