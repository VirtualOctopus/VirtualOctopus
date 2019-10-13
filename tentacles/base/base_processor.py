from contents.base_content import BaseContent
from uri import URI


class BaseTargetProcessor(object):

    """
    Describe a resource meta information, e.g. An URL

    status: initialized -> retrieved
    """

    def get_uri(self) -> URI:
        raise NotImplementedError

    def is_target_retrieved(self) -> bool:
        raise NotImplementedError

    def do_retrieve(self) -> None:
        raise NotImplementedError

    def get_target_content(self) -> BaseContent:
        """
        get target content, if not retrieved, retrieve it firstly
        """
        raise NotImplementedError

    def get_next_targets(self):
        """
        get next targets, if not retrieved, retrieve it firstly
        """
        raise NotImplementedError
