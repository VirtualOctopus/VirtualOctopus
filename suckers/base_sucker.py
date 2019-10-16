from uri import URI

from contents.base_content import BaseContent

from typing import List


class BaseSucker(object):

    """
    configurable data downloader

    like http downloader, SFTP downloader
    """

    @classmethod
    def get_schema(cls) -> str:
        """
        get schema name
        """
        raise NotImplementedError

    def get_contents(self, uri: URI, options: dict) -> List[BaseContent]:
        """
        get contents

        it maybe return multi contents,
        cause single uri contains multi contents
        """
        raise NotImplementedError
