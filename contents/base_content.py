

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
