import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


PACKAGE = "phileo"
NAME = "phileo"
DESCRIPTION = "a liking app"
AUTHOR = "Pinax Team"
AUTHOR_EMAIL = "team@pinaxproject.com"
URL = "http://github.com/pinax/phileo"
VERSION = "1.3"


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.rst"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    package_data={
        "phileo": [
            "templates/phileo/_like.html",
            "templates/phileo/_widget.html",
            "templates/phileo/_widget_brief.html"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    test_suite="runtests.runtests",
    tests_require=[
    ],
    zip_safe=False,
)
