import unittest

from suckers.http_sucker import HTTPSucker

from uri import URI


class HTTPSuckerTest(unittest.TestCase):

    def setUp(self):
        self.sucker = HTTPSucker()

    def test_http_get(self):
        content = self.sucker.get_content(
            URI("https://baidu.com"), {"method": "get"})
        self.assertEqual(content.get_header("content-type"), "text/html")
        self.assertEqual(content.get_status_code(), 200)
