import unittest

from octopus.suckers.http_sucker import HTTPSucker

from uri import URI


class HTTPSuckerTest(unittest.TestCase):

    def setUp(self):
        self.sucker = HTTPSucker()

    def test_http_get(self):
        content = self.sucker.get_contents(
            URI("https://www.qq.com"), {"method": "get"})[0]
        self.assertEqual(content.get_header("content-type"),
                         "text/html; charset=GB2312")
        self.assertEqual(content.get_status_code(), 200)
