from setuptools import find_packages, setup

LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-likes.svg
    :target: https://pypi.python.org/pypi/pinax-likes/

===========
Pinax Likes
===========

.. image:: https://img.shields.io/pypi/v/pinax-likes.svg
    :target: https://pypi.python.org/pypi/pinax-likes/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/pinax-likes/

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-likes.svg
    :target: https://circleci.com/gh/pinax/pinax-likes
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-likes.svg
    :target: https://codecov.io/gh/pinax/pinax-likes
.. image:: https://img.shields.io/github/contributors/pinax/pinax-likes.svg
    :target: https://github.com/pinax/pinax-likes/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-likes.svg
    :target: https://github.com/pinax/pinax-likes/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-likes.svg
    :target: https://github.com/pinax/pinax-likes/pulls?q=is%3Apr+is%3Aclosed

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/


``pinax-likes`` is a liking app for Django, allowing users to "like" and "unlike"
any model instance in your project. Template tags provide the ability to see who
liked an object, what objects a user liked, and more.


Supported Django and Python Versions
------------------------------------

* Django 1.8, 1.10, 1.11, and 2.0
* Python 2.7, 3.4, 3.5, and 3.6
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a liking app for Django",
    name="pinax-likes",
    long_description=LONG_DESCRIPTION,
    version="2.2.1",
    url="http://github.com/pinax/pinax-likes/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "likes": [
        ]
    },
    install_requires=[
        "django-appconf>=1.0.1",
    ],
    test_suite="runtests.runtests",
    tests_require=[
        "mock>=1.3.0",
        "pinax-theme-bootstrap>=7.8.0",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)
