Release History
===============

0.2.0 (2017-10-09)
******************

This release has no changes to the public API, but adds support for Python 2.7 and Python 3.4 to 3.6.

0.1.6 (2017-08-19)
******************

- Fix a bug where ``crawl()`` would crash if it encountered an invalid URL scheme (e.g. ``mailto:`` links).

0.1.5 (2017-02-09)
******************

- Remove a stray ``print()`` statement from inside ``crawl()``.

0.1.4 (2017-02-09)
******************

This release is equivalent to 0.1.3, and just serves as a test of Travis deployments to PyPI.

0.1.3 (2017-02-09)
******************

- Add the ``ignore_fragments`` parameter to ``crawl()``.

0.1.2 (2016-08-10)
******************

- Add the ability to follow ``@font-face`` rules in CSS stylesheets.

0.1.1 (2016-07-07)
******************

- Add the ``follow_external_links`` parameter to ``crawl()``.

0.1.0 (2016-06-09)
******************

- First release!
