import unittest

import http_crawler


class SpiderTest(unittest.TestCase):
    def test_crawl(self):
        self.assertEqual(http_crawler.crawl(), 'hello world')


if __name__ == '__main__':
    unittest.main()
