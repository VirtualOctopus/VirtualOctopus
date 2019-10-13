
from contents.base_content import BaseContent


class HTTPContent(BaseContent):

    def __init__(self, content: str, headers: dict, res_status: int):
        self.headers = headers
        self.content = content
        self.response_status_code = res_status

    def get_type(self):
        return "http_content"

    def get_header(self, header_name) -> dict:
        return self.headers.get(header_name)

    def get_status_code(self) -> int:
        return self.response_status_code
