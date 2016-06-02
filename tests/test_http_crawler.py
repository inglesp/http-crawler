from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
from multiprocessing import Process

import http_crawler


def test_crawl():
    def _serve(dir, port):
        base_dir = os.path.join('tests', dir)
        os.chdir(base_dir)
        server = HTTPServer(('', port), SimpleHTTPRequestHandler)
        server.serve_forever()

    Process(target=_serve, args=('site', 8000), daemon=True).start()
    Process(target=_serve, args=('external-site', 8001), daemon=True).start()

    rsps = list(http_crawler.crawl('http://localhost:8000/'))

    assert len(rsps) == 11

    urls = [rsp.url for rsp in rsps]

    assert len(urls) == len(set(urls))
    assert set(urls) == {
        'http://localhost:8000/',
        'http://localhost:8000/pages/page-1/',
        'http://localhost:8000/pages/page-2/',
        'http://localhost:8000/pages/page-3/',
        'http://localhost:8000/assets/styles.css',
        'http://localhost:8000/assets/styles-2.css',
        'http://localhost:8000/assets/image.jpg',
        'http://localhost:8000/assets/script.js',
        'http://localhost:8000/assets/tile-1.jpg',
        'http://localhost:8000/assets/tile-2.jpg',
        'http://localhost:8001/pages/page-1/',
    }


def test_extract_urls_from_html():
    with open(os.path.join('tests', 'site', 'index.html')) as f:
        content = f.read()

    urls = http_crawler.extract_urls_from_html(content)

    assert len(urls) == 8
    assert set(urls) == {
        '/',
        'http://localhost:8000/pages/page-1',
        'http://localhost:8001/pages/page-1',
        '/pages/page-2',
        'pages/page-3',
        '/assets/styles.css',
        '/assets/image.jpg',
        '/assets/script.js',
    }


def test_extract_urls_from_css():
    with open(os.path.join('tests', 'site', 'assets', 'styles.css')) as f:
        content = f.read()

    urls = http_crawler.extract_urls_from_css(content)

    assert len(urls) == 2
    assert set(urls) == {
        '/assets/styles-2.css',
        '/assets/tile-1.jpg',
    }
