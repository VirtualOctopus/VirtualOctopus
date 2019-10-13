

class BaseContent(object):

    """

    content container

    contains document data

    cleaning data

    """

    def get_type(self) -> str:
        raise NotImplementedError
