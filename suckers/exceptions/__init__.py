
class SuckerBaseException(BaseException):
    pass


class NotFoundException(SuckerBaseException):
    pass


class AuthException(SuckerBaseException):
    pass


class NetworkException(SuckerBaseException):
    pass
