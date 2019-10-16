from typing import List
from enum import Enum, unique


@unique
class ContentType(Enum):

    """
    content type enum
    """

    http = "http_content"


@unique
class ContentAttributeType(Enum):

    """
    content attr type enum
    """

    title = "title"
    author = "author"
    ref = "ref"
    created_date = "created_date"
    updated_date = "updated_date"
    uri = "uri"
    summary = "summary"
    positive = "positive"
    main_language = "main_language"


class ContentAttribute(object):

    def get_type(self):
        return self.type

    def get_value(self):
        return self.value


class BaseContent(object):

    """

    content container

    contains document data

    cleaning data

    """

    def get_type(self) -> str:
        """
        get type
        """
        raise NotImplementedError

    def release_resource(self):
        """
        release current content (from dist/memory/db ...)
        """
        raise NotImplementedError

    def get_content(self) -> str:
        """
        get free text content
        """
        raise NotImplementedError

    def get_attributes(self) -> List[ContentAttribute]:
        raise NotImplementedError

    def get_uris(self):
        """
        get uris from this content
        """
        raise NotImplementedError
