from setuptools import find_packages, setup

import os
import re


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, *parts)) as f:
        return f.read()

VERSION = re.search(
    "^__version__ = '(.*)'$",
    read('src', 'http_crawler', '__init__.py'),
    re.MULTILINE
).group(1)

if __name__ == '__main__':
    setup(
        name='http-crawler',
        version=VERSION,
        description='A library for crawling websites',
        long_description=read('README.rst'),
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        install_requires=['lxml', 'requests', 'tinycss'],
        url='http://github.com/inglesp/http-crawler',
        author='Peter Inglesby',
        author_email='peter.inglesby@gmail.com',
        license='License :: OSI Approved :: MIT License',
    )
