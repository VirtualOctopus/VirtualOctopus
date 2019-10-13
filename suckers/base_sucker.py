from uri import URI

from contents.base_content import BaseContent


class BaseSucker(object):

    """
    configurable data downloader

    like http downloader, SFTP downloader
    """

    @classmethod
    def get_schema(self) -> str:
        """
        get schema name
        """
        raise NotImplementedError

    def get_content(self, uri: URI, options: dict) -> BaseContent:
        """
        get content
        """
        raise NotImplementedError
