http-crawler
============

http-crawler is a library for crawling websites.  It uses requests_ to speak HTTP.


Installation
~~~~~~~~~~~~

Install with pip_:

.. code-block:: console

    $ pip install http-crawler


Usage
~~~~~

The ``http_crawler`` module provides one generator function, ``crawl``.

``crawl`` is called with a URL, and yields instances of requests_'s |Response|_ class.

``crawl`` will request the page at the given URL, and will extract all URLs from the response.  It will then make a request for each of those URLs, and will repeat the process until it has requested every URL linked to from pages on the original URL's domain.  It will not extract or process URLs from any page with a different domain to the original URL.

For instance, this is how you would use ``crawl`` to find and log any broken links on a site:

.. code-block:: pycon

    >>> from http_crawler import crawl
    >>> for rsp in crawl('http://www.example.com'):
    >>>     if rsp.status_code != 200:
    >>>         print('Got {} at {}'.format(rsp.status_code, rsp.url))


Motivation
~~~~~~~~~~

Why another crawling library?  There are certainly lots of Python tools for crawling websites, but all that I could find were either too complex, too simple, or had too many dependencies.

http-crawler is designed to be a `library and not a framework`_, so it should be straightforward to use in applications or other libraries.


Contributing
~~~~~~~~~~~~

There are a handful of enhancements on the `issue tracker`_ that would be suitable for somebody looking to contribute to Open Source for the first time.

For instructions about making Pull Requests, see `GitHub's guide`_.

All contributions should include tests with 100% code coverage, and should comply with `PEP 8`_.  The project uses tox_ for running tests and checking code quality metrics.

To run the tests:

.. code-block:: console

    $ tox


.. _requests: http://docs.python-requests.org/en/master/
.. _pip: https://pip.pypa.io/en/stable/
.. |Response| replace:: ``Response``
.. _Response: http://docs.python-requests.org/en/master/api/#requests.Response
.. _`library and not a framework`: http://tomasp.net/blog/2015/library-frameworks/
.. _`issue tracker`: https://github.com/inglesp/http-crawler/issues
.. _`GitHub's guide`: https://help.github.com/articles/using-pull-requests/
.. _`PEP 8`: https://www.python.org/dev/peps/pep-0008/
.. _tox: https://tox.readthedocs.io/en/latest/
