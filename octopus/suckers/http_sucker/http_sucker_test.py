import unittest

from octopus.suckers.http_sucker.http_sucker import HTTPSucker

from uri import URI
from mimetypes import guess_type


class HTTPSuckerTest(unittest.TestCase):

    def setUp(self):
        self.sucker = HTTPSucker()

    def test_http_get(self):
        content = self.sucker.get_contents(
            URI("https://www.qq.com"), {"method": "get"})[0]
        self.assertEqual(content.get_header("content-type"),
                         "text/html; charset=GB2312")
        self.assertEqual(content.get_status_code(), 200)

    def test_mime_types(self):

        # text
        self.assertEqual(guess_type("hello.html"), ("text/html", None))
        self.assertEqual(guess_type("hello.xml"), ("application/xml", None))
        self.assertEqual(guess_type("hello.json"), ("application/json", None))

        # pdf
        self.assertEqual(guess_type("hello.pdf"), ("application/pdf", None))

        # office
        self.assertEqual(guess_type("hello.doc"), ("application/msword", None))
        self.assertEqual(guess_type("hello.docx"), ("application/vnd.openxmlformats-officedocument.wordprocessingml.document", None))
        self.assertEqual(guess_type("hello.xls"), ("application/vnd.ms-excel", None))
        self.assertEqual(guess_type("hello.xlsx"), ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", None))
        self.assertEqual(guess_type("hello.ppt"), ("application/vnd.ms-powerpoint", None))
        self.assertEqual(guess_type("hello.pptx"), ("application/vnd.openxmlformats-officedocument.presentationml.presentation", None))

        # image
        self.assertEqual(guess_type("hello.png"), ("image/png", None))
        self.assertEqual(guess_type("hello.jpg"), ("image/jpeg", None))
        self.assertEqual(guess_type("hello.jpeg"), ("image/jpeg", None))
