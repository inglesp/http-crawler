import cgi
from urllib.parse import urljoin, urlparse

import lxml.html
import requests
import tinycss


__version__ = '0.1.1'


def crawl(base_url, follow_external_links=True):
    base_netloc = urlparse(base_url).netloc

    seen = set([base_url])
    todo = [base_url]

    session = requests.Session()

    while todo:
        url = todo.pop()
        rsp = session.get(url)

        yield rsp

        if urlparse(url).netloc != base_netloc:
            continue

        content_type, _ = cgi.parse_header(rsp.headers['content-type'])

        if content_type == 'text/html':
            urls = extract_urls_from_html(rsp.text)
        elif content_type == 'text/css':
            urls = extract_urls_from_css(rsp.text)
        else:
            # see https://bitbucket.org/ned/coveragepy/issues/497/
            continue  # pragma: no cover

        for url1 in urls:
            abs_url = urljoin(url, url1)

            if not follow_external_links:
                if urlparse(abs_url).netloc != base_netloc:
                    continue

            if abs_url not in seen:
                seen.add(abs_url)
                todo.append(abs_url)


def extract_urls_from_html(html):
    dom = lxml.html.fromstring(html)
    return dom.xpath('//@href|//@src')


def extract_urls_from_css(css):
    urls = []
    parser = tinycss.make_parser()
    stylesheet = parser.parse_stylesheet(css)
    for rule in stylesheet.rules:
        if rule.at_keyword is None:
            for declaration in rule.declarations:
                for token in declaration.value:
                    if token.type == 'URI':
                        urls.append(token.value)
        elif rule.at_keyword == '@import':
            urls.append(rule.uri)

    return urls
